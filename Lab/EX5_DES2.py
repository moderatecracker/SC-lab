import pyDes
import binascii

# Function to encrypt data
def encrypt(plain_text, key):
    des = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)  # Create DES cipher
    encrypted_text = des.encrypt(plain_text)  # Encrypt
    return binascii.hexlify(encrypted_text).decode()  # Convert to hex

# Function to decrypt data
def decrypt(encrypted_text, key):
    des = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)  # Create DES cipher
    decrypted_text = des.decrypt(binascii.unhexlify(encrypted_text)).decode()  # Decrypt
    return decrypted_text

# Example usage
if __name__ == "__main__":
    key = b"8bytekey"  # DES key must be exactly 8 bytes
    text = "HelloDES"

    print("Original Text:", text)
    
    encrypted = encrypt(text, key)
    print("Encrypted Text:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decrypted Text:", decrypted)
