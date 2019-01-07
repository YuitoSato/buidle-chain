import sys

from flask import Flask, request

from app.controllers.transaction_controller import TransactionController
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




if __name__ == '__main__':
    if sys.argv is not None and sys.argv[1] is not None:
        port = int(sys.argv[1])
        app.run(host = '0.0.0.0', port = port)
    else:
        port = int(sys.argv[1])
        app.run(host = '0.0.0.0', port = 5000)
