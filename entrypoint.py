import sys

from flask import Flask, request

from app.controllers.block_controller import BlockController
from app.controllers.transaction_controller import TransactionController
from app.controllers.tx_output_controller import TxOutputController
from app.utils.buidle_chain_encoder import BuidleChainEncoder


def create_app():
    _app = Flask(__name__)
    _app.config.from_pyfile('app/conf/config.py')

    _app.json_encoder = BuidleChainEncoder

    return _app


app = create_app()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/transactions', methods = ['POST'])
def create_transaction():
    return TransactionController.create_transaction(request)


@app.route('/transactions/unconfirmed')
def fetch_all_unconfirmed_transactions():
    return TransactionController.fetch_all_unconfirmed_transactions()


@app.route('/transactions/utxo', methods = ['POST'])
def fetch_unspent_tx_outputs_by_address():
    return TxOutputController.fetch_unspent_tx_outputs_by_address(request)


@app.route('/mine')
def mine():
    node_number = str(app.config['NODE_NUMBER'])
    node_url = 'http://node' + node_number + ':500' + node_number
    miner_address = app.config['NODE_ADDRESS']
    return BlockController.mine(node_url, miner_address)


@app.route('/blocks/receive', methods = ['POST'])
def receive_block():
    return BlockController.receive_block(request)

@app.route('/blocks')
def fetch_all_blocks():
    return BlockController.fetch_all_blocks()



if __name__ == '__main__':
    if sys.argv is not None and sys.argv[1] is not None:
        port = int(sys.argv[1])
        app.run(host = '0.0.0.0', port = port)
    else:
        port = int(sys.argv[1])
        app.run(host = '0.0.0.0', port = 5000)
