from app.models.block import Block
from app.models.block_receive_request import BlockReceiveRequest
from app.models.proof_result import ProofResult
from app.models.transaction import Transaction
from app.models.transaction_input import TransactionInput
from app.models.transaction_output import TransactionOutput
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

def decode_transaction(dictionary):
    return Transaction(
        transaction_id = dictionary['transaction_id'],
        locktime = dictionary['locktime'],
        tx_inputs = list(map(lambda tx_i: decode_tx_input(tx_i), dictionary['tx_inputs'])),
        tx_outputs = list(map(lambda tx_o: decode_tx_output(tx_o), dictionary['tx_outputs']))
    )

def decode_tx_output(dictionary):
    return TransactionOutput(
        transaction_output_id = dictionary['transaction_output_id'],
        amount = dictionary['amount'],
        locking_script = dictionary['locking_script'],
        sender_address = dictionary['sender_address'],
        recipient_address = dictionary['recipient_address']
    )

def decode_tx_input(dictionary):
    return TransactionInput(
        transaction_input_id = dictionary['transaction_input_id'],
        transaction_output_id = dictionary['transaction_output_id'],
        unlocking_script = dictionary['unlocking_script'],
        amount = dictionary['amount']
    )

def decode_block_receive_request(dictionary):
    return BlockReceiveRequest(
        block = decode_block(dictionary['block']),
        proof_result = decode_proof_result(dictionary['proof_result']),
        sender_node_url = dictionary['sender_node_url'],
        tx_to_miner = decode_transaction(dictionary['tx_to_miner'])
    )

def decode_proof_result(dictionary):
    return ProofResult(
        result_hash_int = dictionary['result_hash_int'],
        target_hash_int = dictionary['target_hash_int'],
        nonce = dictionary['nonce']
    )

def decode_block(dictionary):
    return Block(
        block_id = dictionary['block_id'],
        block_number = dictionary['block_number'],
        previous_block_hash = dictionary['previous_block_hash'],
        timestamp = dictionary['timestamp'],
        merkle_root = dictionary['merkle_root'],
        difficulty_target = dictionary['difficulty_target'],
        nonce = dictionary['nonce'],
        transactions = list(map(lambda tx_dict: decode_transaction(tx_dict), dictionary['transactions']))
    )
