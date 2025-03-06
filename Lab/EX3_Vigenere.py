def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            k = ord(key[i % key_length]) - ord('A')
            shifted = (ord(char) - base + k) % 26
            ciphertext += chr(shifted + base)
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            k = ord(key[i % key_length]) - ord('A')
            shifted = (ord(char) - base - k) % 26
            plaintext += chr(shifted + base)
        else:
            plaintext += char
    return plaintext

plain = "HELLO WORLD"
key = "KEY"
encrypted = vigenere_encrypt(plain, key)
decrypted = vigenere_decrypt(encrypted, key)
print("\nVigenère Cipher:")
print("Plaintext: ", plain)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)