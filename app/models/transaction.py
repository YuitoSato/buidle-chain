import hashlib

from app.models.transaction_input import TransactionInput
from app.models.transaction_output import TransactionOutput
from app.utils.constants import COINBASE_ADDRESS


class Transaction:
    def __init__(self, transaction_id, locktime, tx_outputs, tx_inputs):
        self.transaction_id = transaction_id
        self.locktime = locktime
        self.tx_outputs = tx_outputs
        self.tx_inputs = tx_inputs

    @classmethod
    def build(cls, locktime, timestamp, tx_inputs, request_amount, sender_address, recipient_address):
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

        return Transaction(
            transaction_id = hashlib.sha256((str(locktime) + str(timestamp)).encode('utf-8')).hexdigest(),
            locktime = locktime,
            tx_outputs = [
                to_sender_transaction_output,
                to_coinbase_output,
                to_recipient_output
            ],
            tx_inputs = tx_inputs
        )
