from app.models.transaction import Transaction
from app.models.transaction_input import TransactionInput
from app.stores.blockchain import Blockchain
from app.stores.unconfirmed_tx_pool import UnconfirmedTxPool


class TransactionService:
    @classmethod
    def create_transaction(cls, tx_request):
        # 使用としているトランザクションアウトプットIDが既に未承認のトランザクションアウトプットIDに含まれていたら例外を投げる
        spent_tx_output_ids_in_unconfirmed_tx_pool = UnconfirmedTxPool.list_spent_tx_output_ids()
        tx_request.assert_unspent_tx_output_ids(spent_tx_output_ids_in_unconfirmed_tx_pool)

        unspent_tx_outputs_in_blockchain = Blockchain.list_unspent_tx_outputs_by_tx_output_ids(
            tx_request.get_requesting_tx_output_ids())

        # 今回使用しようとしているトランザクションインプットを算出
        tx_inputs = tx_request.get_tx_inputs(unspent_tx_outputs_in_blockchain)

        TransactionInput.verify_tx_inputs(tx_inputs, tx_request.sender_address)

        transaction = Transaction.build(
            locktime = 0,
            timestamp = tx_request.timestamp,
            tx_inputs = tx_inputs,
            request_amount = tx_request.amount,
            sender_address = tx_request.sender_address,
            recipient_address = tx_request.recipient_address
        )

        UnconfirmedTxPool.transactions.append(transaction)

        return transaction
