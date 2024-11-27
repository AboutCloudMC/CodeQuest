
def encrypt(data: bytes, key: bytes) -> bytes:
    data = bytes(data)
    key = bytes(key)
    return bytes([data[i] ^ key[i % len(key)] for i in range(len(data))])

def decrypt(data: bytes, key: bytes) -> bytes:
    data = bytes(data)
    key = bytes(key)
    return encrypt(data, key)

def encryptFile(path: str, key: bytes):
    with open(path, 'rb') as file:
        data = file.read()
        file.close()
    with open(path, 'wb') as file:
        file.write(encrypt(data, key))
        file.close()

def decryptFile(path: str, key: bytes):
    with open(path, 'rb') as file:
        data = file.read()
        file.close()
    with open(path, 'wb') as file:
        file.write(decrypt(data, key))
        file.close()
    