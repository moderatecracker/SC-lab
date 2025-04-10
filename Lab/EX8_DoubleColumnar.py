def columnar_transposition(message, key):
    # Remove spaces and convert to uppercase for consistency
    message = message.replace(" ", "").upper()
    
    # Create key indices
    # Example: KEY -> K=0, E=1, Y=2 -> indices = [1, 0, 2]
    indices = list(range(len(key)))
    indices.sort(key=lambda i: key[i])
    
    # Calculate number of rows needed
    columns = len(key)
    rows = -(-len(message) // columns)  # Ceiling division
    
    # Create the grid (for visualization)
    grid = [['' for _ in range(columns)] for _ in range(rows)]
    
    # Fill the grid row by row
    pos = 0
    for i in range(rows):
        for j in range(columns):
            if pos < len(message):
                grid[i][j] = message[pos]
                pos += 1
    
    # Read off the message column by column according to the key
    result = ''
    for idx in indices:
        for i in range(rows):
            if i < rows and idx < columns and grid[i][idx]:
                result += grid[i][idx]
    
    return result

def double_columnar_encrypt(plaintext, key1, key2):
    # First transposition
    intermediate = columnar_transposition(plaintext, key1)
    
    # Second transposition
    ciphertext = columnar_transposition(intermediate, key2)
    
    return ciphertext

def double_columnar_decrypt(ciphertext, key1, key2):
    # For decryption, we need to invert the keys
    # This is done by sorting the keys and using the positions
    inverse_key1 = get_inverse_key(key1)
    inverse_key2 = get_inverse_key(key2)
    
    # First apply the inverse of the second key
    intermediate = columnar_transposition(ciphertext, inverse_key2)
    
    # Then apply the inverse of the first key
    plaintext = columnar_transposition(intermediate, inverse_key1)
    
    return plaintext

def get_inverse_key(key):
    # For decryption in columnar transposition, we need the inverse key
    # Create a list of (character, position) pairs
    positions = [(char, i) for i, char in enumerate(key)]
    
    # Sort by characters
    positions.sort()
    
    # The inverse key is the positions in sorted order
    inverse_key = ''.join([str(pos) for _, pos in positions])
    
    return inverse_key

# Example usage
if __name__ == "__main__":
    message = "SASHI"
    key1 = "FIRST"
    key2 = "SECOND"
    
    print("Original message:", message)
    
    # Encrypt
    encrypted = double_columnar_encrypt(message, key1, key2)
    print("Encrypted message:", encrypted)
