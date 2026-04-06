import base64
import os
import sys
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

def generate_key(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(password, input_file, output_file):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    f = Fernet(key)

    with open(input_file, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    with open(output_file, "wb") as file:
        file.write(salt + encrypted)

    print(f"✅ File terenkripsi: {output_file}")

def decrypt_file(password, input_file, output_file):
    with open(input_file, "rb") as file:
        raw = file.read()

    salt = raw[:16]
    encrypted = raw[16:]

    key = generate_key(password, salt)
    f = Fernet(key)

    try:
        decrypted = f.decrypt(encrypted)
    except Exception:
        print("❌ Password salah atau file rusak!")
        return

    with open(output_file, "wb") as file:
        file.write(decrypted)

    print(f"🔓 File berhasil didekripsi: {output_file}")

# CLI
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage:")
        print("Encrypt : python encrypt_file.py enc input.txt output.enc password")
        print("Decrypt : python encrypt_file.py dec input.enc output.txt password")
        sys.exit(1)

    mode = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    password = sys.argv[4]

    if mode == "enc":
        encrypt_file(password, input_file, output_file)
    elif mode == "dec":
        decrypt_file(password, input_file, output_file)
    else:
        print("Mode harus 'enc' atau 'dec'")