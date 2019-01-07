from app.models.transaction_request import TransactionRequest
from app.models.tx_input_request import TxInputRequest


def decode_transaction_request(dictionary):
    return TransactionRequest(
        sender_address = dictionary['sender_address'],
        recipient_address = dictionary['recipient_address'],
        amount = dictionary['amount'],
        timestamp = dictionary['timestamp'],
        tx_input_requests = list(map(decode_tx_input_request, dictionary['tx_input_requests']))
    )


def decode_tx_input_request(dictionary):
    return TxInputRequest(
        transaction_output_id = dictionary['transaction_output_id'],
        unlocking_script = dictionary['unlocking_script'],
    )
