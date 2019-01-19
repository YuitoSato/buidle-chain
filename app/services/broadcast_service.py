import json

import requests

from app.stores.peer_node_store import PeerNodeStore
from app.utils.buidle_chain_encoder import BuidleChainEncoder


class BroadcastService:
    HEADERS = { 'content-type': 'application/json' }

    @classmethod
    def broadcast_tx_request(cls, tx_request):
        nodes = PeerNodeStore.fetch_all_peer_nodes()

        for node in nodes:
            requests.post(node.url + '/transactions', data = json.dumps(tx_request, cls = BuidleChainEncoder), headers = cls.HEADERS)

    @classmethod
    def broadcast_block(cls, block, proof_result, sender_node_url, tx_to_miner):
        nodes = PeerNodeStore.fetch_all_peer_nodes()

        payload = {
            'block': block,
            'proof_result': proof_result,
            'sender_node_url': sender_node_url,
            'tx_to_miner': tx_to_miner
        }

        for node in nodes:
            requests.post(node.url + '/blocks/receive', data = json.dumps(payload, cls = BuidleChainEncoder), headers = cls.HEADERS)
