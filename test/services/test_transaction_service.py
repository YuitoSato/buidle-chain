from unittest import TestCase

from app.services.transaction_service import TransactionService
from app.stores.unconfirmed_tx_pool import UnconfirmedTxPool
from app.utils.buidle_chain_decoder import decode_transaction_request


class TestTransactionService(TestCase):
    def test_create_transaction(self):
        request = {
            'sender_address': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4JL8ek8HCgS6yvTSjog/pfB7vc693fB1AA+8kBRchj51ktejPrR5mRpoMJwzBcgal9sAgLjj1gOa9pLReCfTRWuO+M0BiRJac1ebtAY5/A3dR52fE7U47/Agmm3qjL1Wqr3dbckrwgAHioA7RqhWqPQCl1m3qL66T9YlmvJxICzWX5+9ZQEcxSSyKT5gSBOoCWpE1aJlf8g6xoYSxRoTkES6AXDlYQh63eNeWIZXrOsf/0GEAlYxmLTh5QvNfIbN+Txck913ZP1DX8oQHJC4NKQNwAB+I0BovgJ71aFt3V7CeUN1+dYLbp/UcILfiZEyrbL1cRX6KHXH4HP/RTyjQwIDAQAB',
            'recipient_address': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxnrb17FTtrgfg33ADcbcb2D7mGX+sBIn6jE24ADNKbAvqRuhonnBJxG5W21xMyfP43P4JS8Kb/e6MsdS0D5cwnvRmsgYZdCL9CvzMJ7gYGpaQ174S3ocdTveYVaMnnZExh8OCvfdGFs5O+wdBJF11jhUmKaNAS45LWjYjou3db5oJdd87ISEHOmyB1UOp4bSIvF0EI5zHMS/kXE53t2W95PdsiXStj0HpzBp0C3jwzVLGDuyvALeC6ACg+9R6exBut8mjoDgL47m3/irFy0E2XEhmmRlpxH/hvFkGVvjMIEXBwdc+p1FDNQtGXEUkCWaBiQxNE+TE02qXlsQi6S+IwIDAQAB',
            'amount': 100,
            'timestamp': 0,
            'tx_input_requests': [
                {
                    'transaction_output_id': '38927c5472ba46709f43a750e666ddb1f218fb6b8ec3227a931328e119f8d6a7',
                    'unlocking_script': '35pLa2XoKqIz0agLgeDchHtBg4nYaqJnK6jvwgBoHJyHIgnEnCSo4oo74lJIi48on5CZJLEo0mGCikG7JD4e7J4XhloJNMH4AmvPX5rftdp3yAJH6MPgAQnDDI0zx8gvls88xYzfZYFnUbFscmyKGd5Ehh3SQgjRghnrrykFCybkiwON0jH2rVB1C2xTsyJoaA840ykkl1WsM8NdMQwb4ukBjUP+NLbL6Fw2AH7LQcG/tTpNYSR+VujZoy/bXsaFpmcCtqDcJjvhvzY2vpVBunrm9T9A2ae0RlvuNKK3qbd9I1mAzhwpvWBdMUPInangrK9FjinLB1qEJPvNhC4OXQ=='
                }
            ],
        }

        tx_request = decode_transaction_request(request)

        TransactionService.create_transaction(tx_request)

        self.assertEqual(len(UnconfirmedTxPool.transactions), 1)
