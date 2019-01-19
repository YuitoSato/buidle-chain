from functools import reduce
from operator import add


class UnconfirmedTxPool:
    transactions = []

    @classmethod
    def list_spent_tx_output_ids(cls):
        if len(cls.transactions) == 0:
            return []

        tx_inputs = reduce(add, list(map(lambda tx: tx.tx_inputs, cls.transactions)))
        return list(map(lambda tx_i: tx_i.transaction_output_id, tx_inputs))

    @classmethod
    def create_transaction(cls, transaction):
        cls.transactions.append(transaction)

    @classmethod
    def find_transaction(cls, transaction_id):
        transactions = list(filter(lambda tx: tx.transaction_id == transaction_id, cls.transactions))
        if len(transactions) == 0:
            return None

        return transactions[0]
