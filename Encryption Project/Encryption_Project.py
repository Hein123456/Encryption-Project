import os
import secrets
import tkinter as tk
from tkinter import filedialog
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_file(filename, public_key):
    with open(filename, "rb") as file:
        data = file.read()
    
    encrypted_data = public_key.encrypt(data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        
    encrypted_filename = os.path.splitext(filename)[0] + ".enc"
    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, private_key):
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = private_key.decrypt(encrypted_data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
        
    decrypted_filename = os.path.splitext(filename)[0] + ".dec"
    with open(decrypted_filename, "wb") as file:
        file.write(decrypted_data)

root = tk.Tk()
root.withdraw()

while True:
    print("Please select your option.")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Quit")
    choice = input()
    if choice == "1":
        file_path = filedialog.askopenfilename()
        if file_path:
            private_key, public_key = generate_keys()
            encrypt_file(file_path, public_key)
            private_key_filename = "private_key.pem"
            with open(private_key_filename, "wb") as file:
                file.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()))
            print(f"File '{file_path}' encrypted with public key and saved to '{os.path.abspath(file_path)}.enc'")
            print(f"Private key saved to '{os.path.abspath(private_key_filename)}'")
    elif choice == "2":
        file_path = filedialog.askopenfilename()
        if file_path:
            private_key_filename = filedialog.askopenfilename(title="Select private key file")
            with open(private_key_filename, "rb") as file:
                private_key = serialization.load_pem_private_key(file.read(), password=None)
            decrypt_file(file_path, private_key)
            print(f"File '{file_path}' decrypted and saved to '{os.path.abspath(file_path)}.dec'")
    elif choice == "3":
        break
    else:
        print("Invalid option. Please try again.")
