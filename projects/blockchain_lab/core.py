class BlockchainLab:
    def __init__(self):
        self.wallets = {} # address: private_key
        self.mempool = []
        self.chain = []
        self.difficulty = 2
        self.reward = 50 # AuraCoins
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = self.create_block("Genesis Block", "0")
        block, h = self.mine_block(genesis, self.difficulty)
        block["hash"] = h
        self.chain.append(block)

    def generate_hash(self, text):
        return hashlib.sha256(text.encode()).hexdigest()

    def create_block(self, transactions, previous_hash="0"):
        return {
            "index": len(self.chain),
            "timestamp": time.time(),
            "transactions": transactions,
            "previous_hash": previous_hash,
            "nonce": 0
        }

    def compute_block_hash(self, block):
        # Remove hash if it exists before computing
        b = block.copy()
        if "hash" in b: del b["hash"]
        block_string = json.dumps(b, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, block, difficulty=2):
        target = "0" * difficulty
        while True:
            hash_res = self.compute_block_hash(block)
            if hash_res.startswith(target):
                return block, hash_res
            block["nonce"] += 1

    def generate_wallet(self):
        priv = secrets.token_hex(16)
        pub = "0x" + hashlib.sha256(priv.encode()).hexdigest()[:24]
        self.wallets[pub] = priv
        return pub, priv

    def sign_transaction(self, private_key, transaction_data):
        # Simulated signing: Hash of data + private key
        message = f"{transaction_data}{private_key}"
        return hashlib.sha256(message.encode()).hexdigest()

    def add_tx_to_mempool(self, tx):
        self.mempool.append(tx)
        return len(self.mempool)

    def finalize_mining(self, miner_address):
        # Project 8 & 10: Reward + Mempool processing
        reward_tx = {"sender": "SYSTEM", "receiver": miner_address, "amount": self.reward, "type": "reward"}
        current_txs = [reward_tx] + self.mempool
        
        new_block = self.create_block(current_txs, self.chain[-1]["hash"])
        mined_block, h = self.mine_block(new_block, self.difficulty)
        mined_block["hash"] = h
        
        self.chain.append(mined_block)
        self.mempool = [] # Clear mempool
        return mined_block

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for tx in block["transactions"]:
                if isinstance(tx, dict):
                    if tx.get("receiver") == address:
                        balance += float(tx.get("amount", 0))
                    if tx.get("sender") == address:
                        balance -= float(tx.get("amount", 0))
        return balance

# Global Hub for the 10 Projects
lab_manager = BlockchainLab()
