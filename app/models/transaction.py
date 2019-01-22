import hashlib
from functools import reduce
from operator import add

from app.models.transaction_input import TransactionInput
from app.models.transaction_output import TransactionOutput
from app.utils.constants import COINBASE_ADDRESS


class Transaction:
    def __init__(self, transaction_id, tx_outputs, tx_inputs):
        self.transaction_id = transaction_id
        self.tx_outputs = tx_outputs
        self.tx_inputs = tx_inputs

    @classmethod
    def build(cls, timestamp, tx_inputs, tx_outputs):
        if len(tx_inputs) == 0:
            tx_inputs_hash = ''
        else:
            tx_inputs_hash = reduce(add, list(map(lambda tx_i: tx_i.transaction_input_id, tx_inputs)))

        if len(tx_outputs) == 0:
            tx_outputs_hash = ''
        else:
            tx_outputs_hash = reduce(add, list(map(lambda tx_o: tx_o.transaction_output_id, tx_outputs)))

        transaction_id = hashlib.sha256((str(timestamp)
            + tx_outputs_hash
            + tx_inputs_hash
        ).encode('utf-8')).hexdigest()

        return Transaction(
            transaction_id = transaction_id,
            tx_outputs = tx_outputs,
            tx_inputs = tx_inputs
        )


    @classmethod
    def build_with_tx_outputs(cls, timestamp, tx_inputs, request_amount, sender_address, recipient_address):
        tx_inputs_amount_sum = TransactionInput.calc_total_amount(tx_inputs)

        if request_amount > tx_inputs_amount_sum:
            raise Exception('error.not_enough_input_amount')

        to_sender_amount = request_amount * 0.99

        to_sender_transaction_output = TransactionOutput.build(
            amount = to_sender_amount,
            sender_address = sender_address,
            recipient_address = recipient_address,
            timestamp = timestamp
        )

        to_coinbase_output = TransactionOutput.build(
            amount = request_amount - to_sender_amount,
            sender_address = sender_address,
            recipient_address = COINBASE_ADDRESS,
            timestamp = timestamp
        )

        to_recipient_output = TransactionOutput.build(
            amount = tx_inputs_amount_sum - request_amount,
            sender_address = sender_address,
            recipient_address = sender_address,
            timestamp = timestamp
        )

        tx_outputs = [
            to_sender_transaction_output,
            to_coinbase_output,
            to_recipient_output
        ]

        return cls.build(timestamp, tx_inputs, tx_outputs)

    @classmethod
    def build_for_miner(cls, timestamp, amount, miner_address):
        tx_output = TransactionOutput.build(
            amount = amount,
            sender_address = COINBASE_ADDRESS,
            recipient_address = miner_address,
            timestamp = timestamp
        )
        return Transaction(
            transaction_id = hashlib.sha256(str(timestamp).encode('utf-8')).hexdigest(),
            tx_outputs = [tx_output],
            tx_inputs = []
        )
