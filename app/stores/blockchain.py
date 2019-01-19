from functools import reduce
from operator import add

from app.models.block import Block
from app.models.transaction import Transaction
from app.models.transaction_output import TransactionOutput
from app.utils.constants import COINBASE_ADDRESS


class Blockchain:
    blocks = [
        Block.build(
            block_number = 1,
            previous_block_hash = "1",
            timestamp = 0,
            merkle_root = "",
            difficulty_target = 25,
            nonce = 0,
            transactions = [
                Transaction.build(
                    locktime = 0,
                    timestamp = 1,
                    tx_inputs = [],
                    tx_outputs = [
                        TransactionOutput.build(
                            amount = 1000000000,
                            sender_address = COINBASE_ADDRESS,
                            recipient_address = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB",
                            timestamp = 1
                        )

                    ]
                ),
                Transaction.build(
                    locktime = 0,
                    timestamp = 1,
                    tx_inputs = [],
                    tx_outputs = [
                        TransactionOutput.build(
                            amount = 200000000,
                            sender_address = COINBASE_ADDRESS,
                            recipient_address = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB",
                            timestamp = 1
                        )

                    ]
                ),
                Transaction.build(
                    locktime = 0,
                    timestamp = 1,
                    tx_inputs = [],
                    tx_outputs = [
                        TransactionOutput.build(
                            amount = 300003,
                            sender_address = COINBASE_ADDRESS,
                            recipient_address = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB",
                            timestamp = 1
                        )

                    ]
                ),
            ]
        )
    ]

    @classmethod
    def fetch_all_blocks(cls):
        return cls.blocks

    @classmethod
    def fetch_block_count(cls):
        return len(cls.blocks)

    @classmethod
    def fetch_last_block(cls):
        return cls.blocks[-1]

    @classmethod
    def fetch_unspent_tx_outputs_by_tx_output_ids(cls, tx_output_ids):
        blocks = cls.blocks
        if len(blocks) == 0:
            return []

        transactions = reduce(add, list(map(lambda block: block.transactions, blocks)))
        if len(transactions) == 0:
            return []

        tx_outputs = reduce(add, list(map(lambda tx: tx.tx_outputs, transactions)))

        tx_inputs = reduce(add, list(map(lambda tx: tx.tx_inputs, transactions)))
        spent_tx_output_ids = list(map(lambda tx_i: tx_i.transaction_output_id, tx_inputs))

        unspent_tx_outputs = list(
            filter(lambda tx_o: tx_o.transaction_output_id not in spent_tx_output_ids, tx_outputs))
        return list(filter(lambda tx_o: tx_o.transaction_output_id in tx_output_ids, unspent_tx_outputs))

    @classmethod
    def fetch_unspent_tx_outputs_by_address(cls, address):
        blocks = cls.blocks
        if len(blocks) == 0:
            return []

        transactions = reduce(add, list(map(lambda block: block.transactions, blocks)))
        if len(transactions) == 0:
            return []

        tx_outputs = reduce(add, list(map(lambda tx: tx.tx_outputs, transactions)))
        tx_inputs = reduce(add, list(map(lambda tx: tx.tx_inputs, transactions)))
        spent_tx_output_ids = list(map(lambda tx_i: tx_i.transaction_output_id, tx_inputs))

        return list(filter(
            lambda tx_o: tx_o.recipient_address == address
            and tx_o.transaction_output_id not in spent_tx_output_ids
            , tx_outputs
        ))

    @classmethod
    def create_block(cls, block):
        cls.blocks.append(block)

    @classmethod
    def search_new_transactions(cls, transactions):
        transactions_in_chain = reduce(add, list(map(lambda block: block.transactions, cls.blocks)))
        return list(filter(lambda tx: tx not in transactions_in_chain, transactions))

    @classmethod
    def delete_block(cls, deleting_block):
        cls.blocks.remove(deleting_block)

    @classmethod
    def find_block(cls, block_id):
        blocks = list(filter(lambda block: block.block_id == block_id, cls.blocks))
        if len(blocks) == 0:
            return None
        return blocks[0]
