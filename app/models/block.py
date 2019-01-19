import hashlib
from functools import reduce
from operator import add


class Block:
    def __init__(self, block_id, block_number, previous_block_hash, timestamp, merkle_root, difficulty_target, nonce, transactions):
        self.block_id = block_id
        self.block_number = block_number
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.merkle_root = merkle_root
        self.difficulty_target = difficulty_target
        self.nonce = nonce
        self.transactions = transactions

    @classmethod
    def build(cls, block_number, previous_block_hash, timestamp, merkle_root, difficulty_target, nonce, transactions):
        return Block(
            block_id = hashlib.sha256((
                    previous_block_hash + str(timestamp) + merkle_root + str(difficulty_target) + str(
                    nonce)).encode('utf-8')).hexdigest(),
            block_number = block_number,
            previous_block_hash = previous_block_hash,
            timestamp = timestamp,
            merkle_root = merkle_root,
            difficulty_target = difficulty_target,
            nonce = nonce,
            transactions = transactions
        )

    def get_total_tx_output_amount(self):
        if len(self.transactions) == 0:
            return 0

        tx_outputs = reduce(add, list(map(lambda tx: tx.tx_outputs, self.transactions)))

        if len(tx_outputs) == 0:
            return 0

        tx_output_amounts = list(map(lambda tx_o: tx_o.amount, tx_outputs))

        return reduce(add, tx_output_amounts)

    def get_tx_amount_to_miner(self):
        return self.get_total_tx_output_amount() * 0.99
