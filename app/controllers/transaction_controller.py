from app.services.transaction_service import TransactionService
from app.utils.buidle_chain_decoder import decode_transaction_request


class TransactionController:
    @classmethod
    def create_transaction(cls, request):
        tx_request = decode_transaction_request(request.get_json())
        return TransactionService.create_transaction(tx_request)
