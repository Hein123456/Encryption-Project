import hashlib
from logging import PlaceHolder
from textwrap import fill
import tkinter as tk
from tkinter import ttk

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


root = tk.Tk(className='Python Examples - Frame with Widgets')
root.geometry("1000x500")
root.configure(bg='black')

frame = tk.Frame(master=root, bg='#000000')
frame.pack(pady=20, padx=60)
#row 0
label2 = tk.Label(master=frame, text="Shhhhhh! It's a secret", bg='#000000', fg='#FFFFFF')
label2.grid(row=0, column=2, pady=12, padx=10)
# row 1
label = tk.Label(master=frame, text="File:", relief=tk.RIDGE, bd=2, bg='#DADADA')
label.grid(row=1, column=0, padx=5)

options = ["Option 1", "Option 2", "Option 3"]
dropdown = ttk.Combobox(master=frame, values=options, state='readonly')
dropdown.grid(row=1, column=1, padx=5)

button = tk.Button(master=frame, text="Browse", bg='black', fg='white', relief=tk.RAISED, bd=2)
button.grid(row=1, column=2, padx=5)

#row 2



# Create the label with a bevel
label = ttk.Label(frame, text="Choose an option:", relief="groove", padding=5)
label.grid(row=2, column=0, padx=5, pady=5)

# Create the radio buttons
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
var = tk.StringVar()
var.set(options[0])

for i, option in enumerate(options):
    radio_button = ttk.Radiobutton(frame, text=option, variable=var, value=option)
    radio_button.grid(row=2, column=i+1, padx=5, pady=5)
#row 3





#entry1 = tk.Entry(master=frame, text='key')
#entry1.grid(row=1, column=0, pady=12, padx=10)

#entry2 = tk.Entry(master=frame, text='key2')
#entry2.grid(row=2, column=0, pady=12, padx=10)

root.mainloop()
