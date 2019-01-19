from unittest import TestCase

from app.services.block_service import BlockService
from app.stores.blockchain import Blockchain
from app.stores.unconfirmed_tx_pool import UnconfirmedTxPool


class TestBlockService(TestCase):
    def test_mine(self):
        miner_address = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4JL8ek8HCgS6yvTSjog/pfB7vc693fB1AA+8kBRchj51ktejPrR5mRpoMJwzBcgal9sAgLjj1gOa9pLReCfTRWuO+M0BiRJac1ebtAY5/A3dR52fE7U47/Agmm3qjL1Wqr3dbckrwgAHioA7RqhWqPQCl1m3qL66T9YlmvJxICzWX5+9ZQEcxSSyKT5gSBOoCWpE1aJlf8g6xoYSxRoTkES6AXDlYQh63eNeWIZXrOsf/0GEAlYxmLTh5QvNfIbN+Txck913ZP1DX8oQHJC4NKQNwAB+I0BovgJ71aFt3V7CeUN1+dYLbp/UcILfiZEyrbL1cRX6KHXH4HP/RTyjQwIDAQAB'
        BlockService.mine(miner_address)
        self.assertEqual(len(Blockchain.blocks), 2)
        self.assertEqual(len(UnconfirmedTxPool.transactions), 1)

    def tearDown(self):
        UnconfirmedTxPool.transactions.clear()
