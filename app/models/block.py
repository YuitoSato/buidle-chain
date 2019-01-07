import hashlib


class Block:
    def __init__(self, block_id, block_number, previous_block_hash, timestamp, merkle_root, difficulty_target, nonce, transactions):
        self.block_id = block_id
        self.block_number = block_number
        self.previous_block_hash = previous_block_hash
        self.timestamp = timestamp
        self.merkle_root = merkle_root
        self.difficulty_target = difficulty_target
        self.nonce = nonce
        self.transactions = transactions

    @classmethod
    def build(cls, block_number, previous_block_hash, timestamp, merkle_root, difficulty_target, nonce, transactions):
        return Block(
            block_id = hashlib.sha256((
                    previous_block_hash + str(timestamp) + merkle_root + str(difficulty_target) + str(
                    nonce)).encode('utf-8')).hexdigest(),
            block_number = block_number,
            previous_block_hash = previous_block_hash,
            timestamp = timestamp,
            merkle_root = merkle_root,
            difficulty_target = difficulty_target,
            nonce = nonce,
            transactions = transactions
        )
