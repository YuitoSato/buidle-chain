from json import JSONEncoder

from app.models.block import Block
from app.models.proof_result import ProofResult
from app.models.transaction import Transaction
from app.models.transaction_input import TransactionInput
from app.models.transaction_output import TransactionOutput
from app.models.transaction_request import TransactionRequest
from app.models.tx_input_request import TxInputRequest


class BuidleChainEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Block):
            return {
                'block_id': o.block_id,
                'block_number': o.block_number,
                'previous_block_hash': o.previous_block_hash,
                'timestamp': o.timestamp,
                'merkle_root': o.merkle_root,
                'difficulty_target': o.difficulty_target,
                'nonce': o.nonce,
                'transactions': o.transactions
            }
        if isinstance(o, Transaction):
            return {
                'transaction_id': o.transaction_id,
                'locktime': o.locktime,
                'tx_outputs': o.tx_outputs,
                'tx_inputs': o.tx_inputs
            }
        if isinstance(o, TransactionInput):
            return {
                'transaction_input_id': o.transaction_input_id,
                'transaction_output_id': o.transaction_output_id,
                'unlocking_script': o.unlocking_script,
                'amount': o.amount
            }
        if isinstance(o, TransactionOutput):
            return {
                'transaction_output_id': o.transaction_output_id,
                'amount': o.amount,
                'locking_script': o.locking_script,
                'sender_address': o.sender_address,
                'recipient_address': o.recipient_address
            }
        if isinstance(o, TransactionRequest):
            return {
                'sender_address': o.sender_address,
                'recipient_address': o.recipient_address,
                'amount': o.amount,
                'timestamp': o.timestamp,
                'tx_input_requests': o.tx_input_requests
            }
        if isinstance(o, TxInputRequest):
            return {
                'transaction_output_id': o.transaction_output_id,
                'unlocking_script': o.unlocking_script
            }
        if isinstance(o, ProofResult):
            return {
                'result_hash_int': o.result_hash_int,
                'target_hash_int': o.target_hash_int,
                'nonce': o.nonce
            }
        return JSONEncoder.default(self, o)
