from base64 import b64decode
from functools import reduce

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class TransactionInput:
    def __init__(self, transaction_input_id, transaction_output_id, unlocking_script, amount):
        self.transaction_input_id = transaction_input_id
        self.transaction_output_id = transaction_output_id
        self.unlocking_script = unlocking_script
        self.amount = amount

    def verify(self, sender_address):
        pubkey_str = '-----BEGIN PUBLIC KEY-----\n'\
            + sender_address\
            + '\n-----END PUBLIC KEY-----'

        rsakey = RSA.importKey(pubkey_str.encode('utf-8'))
        signer = PKCS1_v1_5.new(rsakey)
        digest = SHA256.new()
        output_id_str = str(self.transaction_output_id)
        data = output_id_str + ('/' * (-len(str(output_id_str)) % 4))
        digest.update(b64decode(data))

        signer.verify(digest, b64decode(self.unlocking_script))

    @classmethod
    def calc_total_amount(cls, tx_inputs):
        tx_input_amounts = list(map(lambda tx_i: tx_i.amount, tx_inputs))

        if len(tx_inputs) == 0:
            return 0

        return reduce((lambda x, y: x + y), tx_input_amounts)

    @classmethod
    def verify_tx_inputs(cls, tx_inputs, sender_address):
        verify_results = list(map(
            lambda tx_i: tx_i.verify(sender_address), tx_inputs
        ))

        if False in verify_results:
            raise Exception('error.cant_verify_input')
