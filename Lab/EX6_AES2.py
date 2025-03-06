from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def aes_encrypt(plaintext, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode().ljust(16)) + encryptor.finalize()
    return iv + ciphertext  # Prepend IV for use in decryption

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
    return plaintext.decode().strip()

plain = "HELLO AES"
key_aes = b'16bytekeyforaes!'  # 16 bytes for AES-128
encrypted = aes_encrypt(plain, key_aes)
decrypted = aes_decrypt(encrypted, key_aes)

print("\nAES Cipher:")
print("Plaintext: ", plain)
print("Encrypted (hex): ", encrypted.hex())
print("Decrypted: ", decrypted)
