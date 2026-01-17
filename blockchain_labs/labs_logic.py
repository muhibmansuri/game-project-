import hashlib
import time
import secrets
import json

# PROJECT 1: SHA-256 Hashing Lab
def lab1_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# PROJECT 2: Immutable Block Sealer
def lab2_seal(data):
    block = {"timestamp": time.time(), "data": data}
    block_hash = hashlib.sha256(json.dumps(block).encode()).hexdigest()
    return {"block": block, "hash": block_hash}

# PROJECT 3: Nonce Puzzle (Mining)
def lab3_mine(difficulty):
    target = "0" * int(difficulty)
    nonce = 0
    start = time.time()
    while True:
        res = hashlib.sha256(str(nonce).encode()).hexdigest()
        if res.startswith(target):
            return {"nonce": nonce, "hash": res, "time": round(time.time() - start, 4)}
        nonce += 1

# PROJECT 4: Wallet Key Generator
def lab4_wallet():
    priv = secrets.token_hex(32)
    pub = "0x" + hashlib.sha256(priv.encode()).hexdigest()[:40]
    return {"private": priv, "public": pub}

# PROJECT 5: Transaction Verification (Dummy Sign)
def lab5_sign(key, msg):
    # Isolated signing logic
    signature = hashlib.sha256(f"{key}{msg}".encode()).hexdigest()
    return {"signature": signature, "status": "Mathematically Verified"}

# PROJECT 6: Activity History Ledger
# This one uses a local list but doesn't connect to other labs
lab6_history = []
def lab6_add(event):
    timestamp = time.ctime()
    entry = f"[{timestamp}] {event}"
    lab6_history.append(entry)
    return lab6_history[-5:] # Return last 5

# PROJECT 7: Asset Ownership Check
inventory = {"Asset_001": "Alice", "Asset_002": "Bob", "Asset_003": "Charlie"}
def lab7_check(asset_id):
    owner = inventory.get(asset_id, "Unknown / Not Registered")
    return {"asset": asset_id, "owner": owner}

# PROJECT 8: P2P Network Delay Sim
def lab8_broadcast(nodes):
    delays = {f"Node_{i}": f"{secrets.randbelow(100)}ms" for i in range(1, int(nodes)+1)}
    return delays

# PROJECT 9: Validity Checker
def lab9_validate(orig_hash, new_data):
    # Checks if hash matches data
    new_hash = hashlib.sha256(new_data.encode()).hexdigest()
    is_valid = (orig_hash == new_hash)
    return {"status": "Unchanged" if is_valid else "Tampered / Changed", "valid": is_valid}

# PROJECT 10: Coin Tap (Faucet)
def lab10_tap(address):
    # Gives 100 dummy coins for an address
    return {"address": address, "amount": 100, "currency": "Aura", "msg": "Test coins minted successfully"}
