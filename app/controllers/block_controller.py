from flask.json import jsonify

from app.models.errors.duplicated_block_exception import DuplicatedBlockException
from app.models.errors.lose_mining_exception import LoseMiningException
from app.services.block_service import BlockService
from app.services.broadcast_service import BroadcastService
from app.stores.blockchain import Blockchain
from app.utils.buidle_chain_decoder import decode_block_receive_request


class BlockController:
    @classmethod
    def mine(cls, node_url, miner_address):
        try:
            block, proof_result, tx_to_miner = BlockService.mine(miner_address)
        except LoseMiningException as e:
            return jsonify(e.code), 304

        BroadcastService.broadcast_block(block, proof_result, node_url, tx_to_miner)
        return jsonify({}), 201

    @classmethod
    def receive_block(cls, request):
        block_receive_request = decode_block_receive_request(request.get_json())
        block = block_receive_request.block
        proof_result = block_receive_request.proof_result
        sender_node_url = block_receive_request.sender_node_url
        tx_to_miner = block_receive_request.tx_to_miner

        try:
            BlockService.assert_new_block(block.block_id)
        except DuplicatedBlockException as e:
            return jsonify(e.code), 304

        try:
            BlockService.receive_block(block, proof_result, sender_node_url, tx_to_miner)
        except Exception as e:
            return jsonify(e), 400

        BroadcastService.broadcast_block(block, proof_result, sender_node_url, tx_to_miner)
        return jsonify({}), 201

    @classmethod
    def fetch_all_blocks(cls):
        return jsonify(Blockchain.fetch_all_blocks()), 200
