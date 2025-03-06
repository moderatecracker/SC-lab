from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_text, DES.block_size)
    return plaintext.decode()

plain = "HELLO DES"
key_des = b'8bytekey'  # Key must be exactly 8 bytes
encrypted = des_encrypt(plain, key_des)
decrypted = des_decrypt(encrypted, key_des)
print("\nDES Cipher:")
print("Plaintext: ", plain)
print("Encrypted (hex): ", encrypted.hex())
print("Decrypted: ", decrypted)