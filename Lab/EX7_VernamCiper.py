import os

def vernam_encrypt(plaintext, key):
    plaintext_bytes = plaintext.encode('utf-8')
    ciphertext = bytes([b ^ k for b, k in zip(plaintext_bytes, key)])
    return ciphertext

def vernam_decrypt(ciphertext, key):
    plaintext_bytes = bytes([b ^ k for b, k in zip(ciphertext, key)])
    return plaintext_bytes.decode('utf-8')

plain = "HELLO"
key = os.urandom(len(plain))  # Random key of the same length as plaintext
encrypted = vernam_encrypt(plain, key)
decrypted = vernam_decrypt(encrypted, key)
print("\nVernam Cipher (One-Time Pad):")
print("Plaintext: ", plain)
print("Encrypted (hex): ", encrypted.hex())
print("Decrypted: ", decrypted)