import cryptography
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Security Key Generated Successfully!")

def encrypt_data(message):
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    print("Data Encrypted: ", encrypted_message)

# Pinnacle AI University - Sovereign Core Research
print("--- Sovereign Vault Security System ---")
# generate_key() # প্রথমবার চালানোর সময় এটি আনকমেন্ট করুন
