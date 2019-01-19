class BlockReceiveRequest:
    def __init__(self, block, proof_result, sender_node_url, tx_to_miner):
        self.block = block
        self.proof_result = proof_result
        self.sender_node_url = sender_node_url
        self.tx_to_miner = tx_to_miner