from datetime import datetime

import requests

from app.models.block import Block
from app.models.exceptions.duplicated_block_exception import DuplicatedBlockException
from app.models.exceptions.invalid_received_block_exception import InvalidReceivedBlockException
from app.models.exceptions.lose_mining_exception import LoseMiningException
from app.models.exceptions.too_short_received_block_exception import TooShortReceivedBlockException
from app.models.proof_of_work import ProofOfWork
from app.models.transaction import Transaction
from app.stores.blockchain import Blockchain
from app.stores.unconfirmed_tx_pool import UnconfirmedTxPool
from app.utils.buidle_chain_decoder import decode_block


class BlockService:
    @classmethod
    def mine(cls, miner_address):
        block, proof_result = cls._create_block()

        try:
            tx_to_miner = cls._create_tx_to_miner(block, miner_address)
        except LoseMiningException() as e:
            raise e

        return block, proof_result, tx_to_miner

    @classmethod
    def _create_block(cls):
        last_block = Blockchain.fetch_last_block()

        previous_hash = last_block.block_id
        block_number = Blockchain.fetch_block_count() + 1

        proof_of_work = ProofOfWork(previous_hash, last_block.difficulty_target)
        proof_result = proof_of_work.prove()

        proof_result.assert_valid()

        transactions = UnconfirmedTxPool.transactions.copy()
        UnconfirmedTxPool.transactions.clear()

        target_transactions = Blockchain.search_new_transactions(transactions)

        block = Block.build(
            block_number = block_number,
            previous_block_hash = previous_hash,
            timestamp = datetime.now().timestamp(),
            merkle_root = "",  # TODO
            difficulty_target = last_block.difficulty_target,
            nonce = proof_result.nonce,
            transactions = target_transactions
        )

        last_block = Blockchain.fetch_last_block()
        if last_block.block_id != block.previous_block_hash:
            print('lost mining', block.block_id)
            raise LoseMiningException()

        Blockchain.create_block(block)
        print('block created', block.block_id)
        print('current block number', block.block_number)

        return block, proof_result

    @classmethod
    def _create_tx_to_miner(cls, block, miner_address):
        tx_amount_to_miner = block.get_tx_amount_to_miner()
        transaction = Transaction.build_for_miner(
            timestamp = datetime.now().timestamp(),
            amount = tx_amount_to_miner,
            miner_address = miner_address
        )
        UnconfirmedTxPool.create_transaction(transaction)
        return transaction

    @classmethod
    def receive_block(cls, block, proof_result, sender_node_url, tx_to_miner):
        last_block = Blockchain.fetch_last_block()

        if not proof_result.is_valid():
            raise InvalidReceivedBlockException()

        if last_block.block_id != block.previous_block_hash:
            if last_block.block_number < block.block_number:
                print('resolving conflicting...')
                cls._resolve_conflicts(sender_node_url)
            else:
                print('win conflict')
                raise TooShortReceivedBlockException()

        if last_block.block_id == block.previous_block_hash:
            Blockchain.create_block(block)

        UnconfirmedTxPool.transactions.clear()
        UnconfirmedTxPool.create_transaction(tx_to_miner)

    @classmethod
    def _resolve_conflicts(cls, send_node_url):
        json = requests.get(send_node_url + '/blocks').json()
        send_node_blocks = list(map(lambda block_dict: decode_block(block_dict), json))
        my_node_blocks = Blockchain.fetch_all_blocks()

        forked_block_number = cls._search_forked_block_number(send_node_blocks, my_node_blocks)
        deleting_blocks = list(filter(lambda block: block.block_number > forked_block_number, my_node_blocks))
        adding_blocks = list(filter(lambda block: block.block_number > forked_block_number, send_node_blocks))

        for deleting_block in deleting_blocks:
            Blockchain.delete_block(deleting_block)

        for adding_block in adding_blocks:
            Blockchain.create_block(adding_block)

    @classmethod
    def _search_forked_block_number(cls, blocks1, blocks2):
        for block1 in blocks1:
            for block2 in blocks2:
                if block1.block_id == block2.block_id:
                    return block1.block_number
        return 0

    @classmethod
    def assert_new_block(cls, block_id):
        block = Blockchain.find_block(block_id)
        if block is not None:
            raise DuplicatedBlockException()

        return
