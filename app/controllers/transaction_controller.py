from flask.json import jsonify

from app.models.errors.tx_output_already_spent_exception import TxOutputAlreadySpentException
from app.services.broadcast_service import BroadcastService
from app.services.transaction_service import TransactionService
from app.stores.unconfirmed_tx_pool import UnconfirmedTxPool
from app.utils.buidle_chain_decoder import decode_transaction_request


class TransactionController:
    @classmethod
    def create_transaction(cls, request):
        tx_request = decode_transaction_request(request.get_json())

        try:
            transaction = TransactionService.create_transaction(tx_request)
        except TxOutputAlreadySpentException as e:
            return jsonify(e.code), 304

        BroadcastService.broadcast_tx_request(tx_request)
        return jsonify(transaction), 201

    @classmethod
    def fetch_all_unconfirmed_transactions(cls):
        transactions = UnconfirmedTxPool.transactions
        return jsonify(transactions), 201
