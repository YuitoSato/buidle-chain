from functools import reduce
from operator import add


class UnconfirmedTxPool:
    transactions = []

    @classmethod
    def list_spent_tx_output_ids(cls):
        if len(cls.transactions) == 0:
            return []

        tx_inputs = reduce(add, list(map(lambda tx: tx.transaction_inputs, cls.transactions)))
        return list(map(lambda tx_i: tx_i.transaction_output_id, tx_inputs))
