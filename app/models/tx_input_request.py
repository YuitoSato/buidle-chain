class TxInputRequest:
    def __init__(self, transaction_output_id, unlocking_script):
        self.transaction_output_id = transaction_output_id
        self.unlocking_script = unlocking_script

    def to_input(self, unspent_tx_output):
        return unspent_tx_output.to_input(self.unlocking_script)
