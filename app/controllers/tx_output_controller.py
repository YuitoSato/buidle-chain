from flask.json import jsonify

from app.stores.blockchain import Blockchain
from app.stores.unconfirmed_tx_pool import UnconfirmedTxPool


class TxOutputController:
    @classmethod
    def fetch_unspent_tx_outputs_by_address(cls, request):
        address = request.get_json()['address']
        unspent_tx_outputs_in_blockchain = Blockchain.fetch_unspent_tx_outputs_by_address(address)
        result_tx_outputs = list(filter(lambda tx_o: tx_o.transaction_output_id not in UnconfirmedTxPool.list_spent_tx_output_ids(), unspent_tx_outputs_in_blockchain))
        return jsonify(result_tx_outputs), 200
