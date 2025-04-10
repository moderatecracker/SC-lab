# Mobile Security

import hashlib
import base64

def scan_for_malicious_apps(app_list):
    """Scans for malicious apps based on their hashes."""
    known_malicious_apps = [
        "5d41402abc4b2a76b9719d911017c592",  # Example malicious hash
    ]
    malicious_apps = []
    for app in app_list:
        app_hash = hashlib.md5(app.encode()).hexdigest()  # Hashing the app name
        if app_hash in known_malicious_apps:
            malicious_apps.append(app)
    return malicious_apps

def encrypt_data(data):
    """Encrypts data using Base64."""
    return base64.b64encode(data.encode()).decode()

def decrypt_data(encrypted_data):
    """Decrypts Base64 encrypted data."""
    return base64.b64decode(encrypted_data.encode()).decode()

def hash_password(password):
    """Returns the SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user():
    """Asks for username & password twice and ensures they match."""
    username1 = input("Enter username: ").strip()
    password1 = input("Enter password: ").strip()

    username2 = input("Re-enter username for verification: ").strip()
    password2 = input("Re-enter password for verification: ").strip()

    # Hash passwords before comparison
    hashed_password1 = hash_password(password1)
    hashed_password2 = hash_password(password2)

    if username1 == username2 and hashed_password1 == hashed_password2:
        return True
    else:
        return False

# Main Execution
if __name__ == "__main__":
    # Part 1: Scan for malicious apps
    print("=== Part 1: Scan for Malicious Apps ===")
    installed_apps = ["app1", "malicious_app"]
    malicious_apps_found = scan_for_malicious_apps(installed_apps)
    if malicious_apps_found:
        print("⚠ Malicious apps found:", malicious_apps_found)
    else:
        print("✅ No malicious apps found.")

    # Part 2: Secure data storage
    print("\n=== Part 2: Secure Data Storage ===")
    sensitive_data = "This is sensitive information"
    encrypted_data = encrypt_data(sensitive_data)
    decrypted_data = decrypt_data(encrypted_data)
    print(f"Sensitive data: {sensitive_data}")
    print(f"🔐 Encrypted data: {encrypted_data}")
    print(f"🔓 Decrypted data: {decrypted_data}")

    # Part 3: User authentication
    print("\n=== Part 3: User Authentication ===")

    if authenticate_user():
        print("✅ Authentication successful. You are now logged in.")
    else:
        print("❌ Authentication failed. Username or password did not match.")
