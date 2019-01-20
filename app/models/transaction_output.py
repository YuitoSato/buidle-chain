import hashlib
import uuid
from functools import reduce
from operator import add

from app.models.exceptions.not_enough_balance_exception import NotEnoughBalanceException
from app.models.transaction_input import TransactionInput
from app.utils.constants import COINBASE_ADDRESS
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256


class TransactionOutput:
    def __init__(self, transaction_output_id, amount, locking_script, sender_address, recipient_address):
        self.transaction_output_id = transaction_output_id
        self.amount = amount
        self.locking_script = locking_script
        self.sender_address = sender_address
        self.recipient_address = recipient_address

    @classmethod
    def build(cls, amount, sender_address, recipient_address, timestamp):
        transaction_output_id = hashlib.sha256((str(amount) + sender_address + recipient_address + str(timestamp)).encode('utf-8')).hexdigest()

        return TransactionOutput(
            transaction_output_id = transaction_output_id,
            amount = amount,
            locking_script = TransactionOutput.calc_locking_script(recipient_address, transaction_output_id),
            sender_address = sender_address,
            recipient_address = recipient_address
        )

    def to_input(self, unlocking_script):
        return TransactionInput(
            transaction_input_id = uuid.uuid1().hex,
            transaction_output_id = self.transaction_output_id,
            unlocking_script = unlocking_script,
            amount = self.amount
        )

    @classmethod
    def calc_locking_script(cls, recipient_address, transaction_output_id):
        if recipient_address == COINBASE_ADDRESS:
            return COINBASE_ADDRESS
        else:
            public_key_str = '-----BEGIN PUBLIC KEY-----\n'\
                + recipient_address\
                + '\n-----END PUBLIC KEY-----'
            public_key = RSA.importKey(public_key_str.encode('utf-8'))
            encryptor = PKCS1_OAEP.new(public_key, SHA256)
            encrypted = encryptor.encrypt(transaction_output_id.encode('utf-8'))
            return encrypted.decode('latin-1')

    @classmethod
    def calc_total_amount(cls, tx_outputs):
        if len(tx_outputs) == 0:
            return 0

        tx_output_amounts = list(map(lambda tx_o: tx_o.amount, tx_outputs))
        return reduce(add, tx_output_amounts)

    @classmethod
    def fetch_tx_outputs_over_amount(cls, target_amount, tx_outputs):
        result_tx_outputs = []
        sum_amount = 0
        for i in range(len(tx_outputs)):
            result_tx_outputs.append(tx_outputs[i])
            sum_amount += tx_outputs[i].amount
            if sum_amount > target_amount:
                return result_tx_outputs

        raise NotEnoughBalanceException()
