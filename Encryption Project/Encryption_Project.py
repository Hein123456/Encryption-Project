import os
import secrets
import tkinter as tk
from tkinter import filedialog

def encrypt_file(filename, key):
    with open(filename, "rb") as file:
        print(file.read())
        data = file.read()
    
    key_bytes = key.encode()
    encrypted_data = bytearray()
    for i in range(len(data)):
        encrypted_data.append(data[i] ^ key_bytes[i % len(key_bytes)])
        
    encrypted_filename = os.path.splitext(filename)[0] + ".enc"
    with open(encrypted_filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filename, key):
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    
    key_bytes = key.encode()
    decrypted_data = bytearray()
    for i in range(len(encrypted_data)):
        decrypted_data.append(encrypted_data[i] ^ key_bytes[i % len(key_bytes)])
        
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
            key = secrets.token_hex(16)
            encrypt_file(file_path, key)
            print(f"File '{file_path}' encrypted with key: {key}")
    elif choice == "2":
        file_path = filedialog.askopenfilename()
        if file_path:
            key = input("Enter encryption key:\n")
            decrypt_file(file_path, key)
            print(f"File '{file_path}' decrypted.")
    elif choice == "3":
        break
    else:
        print("Invalid option. Please try again.")
