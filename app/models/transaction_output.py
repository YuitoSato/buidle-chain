import hashlib
import uuid

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
