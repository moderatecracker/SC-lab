def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = key % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    # Decryption is just encryption with negative key
    return caesar_encrypt(ciphertext, -key)

# Example usage:
plain = "HELLO WORLD"
key = 3
encrypted = caesar_encrypt(plain, key)
decrypted = caesar_decrypt(encrypted, key)
print("Caesar Cipher:")
print("Plaintext: ", plain)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)