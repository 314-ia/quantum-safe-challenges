from hashlib import sha3_256

def master_key(sigma: int) -> bytes:
    return sha3_256(b'TRIDENT|MASTER|' + sigma.to_bytes(4, 'big')).digest()
