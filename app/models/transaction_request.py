class TransactionRequest:
    def __init__(self, sender_address, recipient_address, amount, timestamp, tx_input_requests):
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.amount = amount
        self.timestamp = timestamp
        self.tx_input_requests = tx_input_requests

    def get_requesting_tx_output_ids(self):
        return list(map(lambda tx_i: tx_i.transaction_output_id, self.tx_input_requests))

    def assert_unspent_tx_output_ids(self, spent_tx_output_ids):
        for tx_output_id in self.get_requesting_tx_output_ids():
            if tx_output_id in spent_tx_output_ids:
                raise Exception('error.requesting_transaction_output_already_spent')

    def get_tx_inputs(self, unspent_tx_outputs):
        tx_inputs = list(map(
            lambda tx_i_request: _tx_output_to_tx_input(unspent_tx_outputs, tx_i_request), self.tx_input_requests
        ))

        if len(list(filter(None, tx_inputs))) == 0:
            raise Exception('error.not_enough_input_amount')

        return tx_inputs


def _tx_output_to_tx_input(unspent_tx_outputs, tx_input_request):
    unspent_tx_outputs = list(filter(
        lambda tx_o: tx_o.transaction_output_id == tx_input_request.transaction_output_id, unspent_tx_outputs
    ))

    if len(unspent_tx_outputs) == 0:
        return None

    return tx_input_request.to_input(unspent_tx_outputs[0])
