import hashlib

def get_hash(data):
    # Isolated logic for SHA-256
    return hashlib.sha256(data.encode()).hexdigest()
