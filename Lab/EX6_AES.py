from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def aes_encrypt(plaintext, key):
    iv = os.urandom(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return iv + ciphertext  # Prepend IV for use in decryption

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    actual_ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(actual_ciphertext), AES.block_size)
    return plaintext.decode()

plain = "HELLO AES"
key_aes = b'16bytekeyforaes!'  # Must be 16 bytes for AES-128
encrypted = aes_encrypt(plain, key_aes)
decrypted = aes_decrypt(encrypted, key_aes)
print("\nAES Cipher:")
print("Plaintext: ", plain)
print("Encrypted (hex): ", encrypted.hex())
print("Decrypted: ", decrypted)