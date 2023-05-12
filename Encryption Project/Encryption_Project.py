import hashlib
import tkinter as tk

def encrypt_xor(data, key):
    return bytes(a ^ b for a, b in zip(data, key))

def encrypt_file_xor(filename, key):
    with open(filename, "rb") as file:
        data = file.read()
    encrypted_data = encrypt_xor(data, key)
    with open("CC-" + filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_xor(data, key):
    return bytes(a ^ b for a, b in zip(data, key))

def decrypt_file_xor(filename, key):
    with open(filename, "rb") as file:
        data = file.read()
    decrypted_data = decrypt_xor(data, key)
    with open("DC-" + filename, "wb") as file:
        file.write(decrypted_data)

def encrypt_hash(data, key):
    hash_key = hashlib.sha256(key.encode()).digest()
    return encrypt_xor(data, hash_key)

def encrypt_file_hash(filename, key):
    with open(filename, "rb") as file:
        data = file.read()
    encrypted_data = encrypt_hash(data, key)
    with open("CC-" + filename, "wb") as file:
        file.write(encrypted_data)

def decrypt_hash(data, key):
    hash_key = hashlib.sha256(key.encode()).digest()
    return decrypt_xor(data, hash_key)

def decrypt_file_hash(filename, key):
    with open(filename, "rb") as file:
        data = file.read()
    decrypted_data = decrypt_hash(data, key)
    with open("DC-" + filename, "wb") as file:
        file.write(decrypted_data)

def user_application():
    choice = ""
    while choice != "4":
        print("Please select your option.")
        print("1. Encrypt File with XOR")
        print("2. Decrypt File with XOR")
        print("3. Encrypt File with Hash")
        print("4. Decrypt File with Hash")
        print("5. Quit")
        choice = input()
        if choice in ["1", "2", "3", "4"]:
            key = input("Enter a key:\n")
            filename = input("Enter filename with extension:\n")
        if choice == "1":
            encrypt_file_xor(filename, key)
            print(f"File '{filename}' encrypted with XOR key: {key}")
        elif choice == "2":
            decrypt_file_xor(filename, key)
            print(f"File '{filename}' decrypted with XOR key: {key}")
        elif choice == "3":
            encrypt_file_hash(filename, key)
            print(f"File '{filename}' encrypted with hash key: {key}")
        elif choice == "4":
            decrypt_file_hash(filename, key)
            print(f"File '{filename}' decrypted with hash key: {key}")
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

#ui 


root = tk.Tk()
root.geometry("500x350")

frame = tk.Frame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = tk.Label(master=frame, text="Shhhhhh! It's a secret")
label.pack(pady=12, padx=10)

root.mainloop()
