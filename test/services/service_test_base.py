# from unittest import TestCase
#
# from app.models.block import Block
# from app.models.transaction import Transaction
# from app.models.transaction_output import TransactionOutput
# from app.stores.blockchain import Blockchain
#
#
# class ServiceTestBase(TestCase):
#     @classmethod
#     def seed(cls):
#         timestamp = 0
#
#         transaction_output = TransactionOutput.build(
#             amount = 10000000000000000000,
#             sender_address = 'coinbase',
#             recipient_address = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAznjoHvzCJtQcIYd3yj7vgwaPlyiG6U/Qlw1G89n0bNt5anvRe+e2eKzvpy98aj6ShGu7hARE9SxAFA9bIHCBqdAyPnrUaw7qGkeZNPHBByHe9prJSn0ZwBtfySOSbzdetO5aAwvLj5qMudW2PDz15mP2taGOvXqNnbcH78ZHQLvF6G+SbwuLHU5LEDSZlcy+CnvPqD67cg+QmJLneVmQfOBtbFHz3yDQghNrHWa+UCspUMHVGsDG6OEK7MSpPieY6TzBEYQWsikosQ+V0zBNrSCADe3GBcJ7XzafM/gb+gzJ1eP78F1sA6Ja4ZtqInqN406PwerAXaUJa2twW6529wIDAQAB',
#             timestamp = timestamp
#         )
#
#         transaction = Transaction(
#             transaction_id = '1',
#             locktime = 0,
#             tx_inputs = [],
#             tx_outputs = [transaction_output]
#         )
#
#         block = Block.build(
#             block_number = 1,
#             previous_block_hash = '1',
#             timestamp = 1,
#             merkle_root = '',
#             difficulty_target = 10,
#             nonce = 1,
#             transactions = transaction
#         )
#
#         Blockchain.blocks.append(block)
#
#     def tearDown(self):
#         Blockchain.blocks.clear()
#
#     def setUp(self):
#         ServiceTestBase.seed()
