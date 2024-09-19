import hashlib

from hash.hash_config import hash_settings


async def create_custom_hash(input_string):
    hash_object = hashlib.sha256(input_string.encode())
    hex_dig = hash_object.hexdigest()

    hash_alphabet_len = len(hash_settings.HASH_ALPHABET)
    return ''.join(hash_settings.HASH_ALPHABET[int(hex_dig[i*2:i*2+2], 16) % hash_alphabet_len] for i in range(6))