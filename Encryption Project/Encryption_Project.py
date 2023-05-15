#GUI Imports
from asyncio.windows_events import NULL
from msilib.schema import RadioButton
import tkinter as tk
from tkinter import Radiobutton, Variable, messagebox, filedialog, font, ttk
import os
import random
# DES Imports
from Crypto.Cipher import DES
# AES Imports
from Crypto.Cipher import AES
#hash
import hashlib
file_name = ''

#main
def run_code():
    if var1.get() == "Default":
        if var2.get() == "Encrypt":
            update_progress(1)
            file_path = entry0.get()
            update_progress(3)
            file_name = os.path.basename(file_path)
            update_progress(6)
            xoe_Encrypt(file_name,text_to_int(entry1.get()))
            update_progress(10)
            listbox2.insert(tk.END,"File encrypted successfully")
        if var2.get() == "Decrypt":
            update_progress(1)
            file_path = entry0.get()
            update_progress(3)
            file_name = os.path.basename(file_path)
            update_progress(6)
            xor_Decrypt(file_name, text_to_int(entry1.get()))
            update_progress(10)
            listbox2.insert(tk.END,"File decrypted successfully")


    if var1.get() == "Custom":
        if var2.get() == "Encrypt":
            update_progress(1)
     
            file_path = entry0.get()
            file_name = os.path.basename(file_path)
            AES_encrypt(file_path,hash_keyword16(rot47_encode(entry1.get())))
            update_progress(3) 
            DES_encrypt(hash_keyword8(rot47_encode(entry1.get())),file_name)
            update_progress(6)
            Remove_file(file_path)
            listbox1.insert(tk.END,"File encrypted successfully")
            Remove_file('CC-')
            update_progress(10)

        if var2.get() == "Decrypt":
            update_progress(1)
            file_path = entry0.get()
            file_name = os.path.basename(file_path)
            update_progress(2)
            DES_decrypt(hash_keyword8(rot47_encode(entry1.get())),file_path)
            update_progress(3)
            AES_decrypt(file_name,hash_keyword16(rot47_encode(entry1.get())), file_name)
            update_progress(6)
            listbox2.insert(tk.END,"File decrypted successfully")
            Remove_file('DD-')
            Remove_file(file_name)
            update_progress(10)
  
#XOR
def xoe_Encrypt(filename, key):
    # Open the input file in binary read mode
    file = open(filename, "rb")
    # Read the data from the file
    data = file.read()
    # Close the input file
    file.close()

    # Convert the data to a mutable bytearray
    data = bytearray(data)

    # XOR each byte of the data with the key
    for index, value in enumerate(data):
        data[index] = value ^ key

    # Create a new file with a prefix "CC-" and write the encrypted data to it
    file = open("CC-" + filename, "wb")
    file.write(data)
    # Close the output file
    file.close()

def xor_Decrypt(filename, key):
    # Open the encrypted file in binary read mode
    file = open(filename, "rb")
    # Read the data from the file
    data = file.read()
    # Close the input file
    file.close()

    # Convert the data to a mutable bytearray
    data = bytearray(data)

    # XOR each byte of the data with the key to decrypt
    for index, value in enumerate(data):
        data[index] = value ^ key

    # Overwrite the original file with the decrypted data
    file = open(filename, "wb")
    file.write(data)
    # Close the output file
    file.close()
   
    
#AES encrypt & decrypt 
def AES_encrypt(file_path, key):
    # Create a new AES cipher object with the given key and EAX mode
    cipher = AES.new(key, AES.MODE_EAX)
    
    # Generate a random nonce (number used once)
    nonce = cipher.nonce
    
    # Read the content of the input file
    with open(file_path, 'rb') as fin:
        plaintext = fin.read()
    
    # Encrypt the plaintext using the cipher
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    
    # Write the encrypted data along with the nonce and tag to a new file
    with open('CC-', 'wb') as fout:
        fout.write(nonce + ciphertext + tag)

def AES_decrypt(file_path, key, file_name):
    # Read the encrypted data from the input file
    with open('DD-', 'rb') as fin:
        data = fin.read()
    
    # Extract the nonce, ciphertext, and tag from the data
    nonce = data[:16]
    ciphertext = data[16:-16]
    tag = data[-16:]
    
    # Create a new AES cipher object with the given key, EAX mode, and nonce
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    
    # Decrypt the ciphertext and verify the authenticity using the tag
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    
    # Write the decrypted plaintext to a new file
    with open('DD-' + file_name, 'wb') as fout:
         fout.write(plaintext)

        
def DES_encrypt(key, file_name):
    # Create a new DES cipher object with the given key and OFB mode
    cipher = DES.new(key, DES.MODE_OFB)

    # Generate a random initialization vector (IV)
    iv = cipher.iv

    # Open the input file for reading and the output file for writing
    with open('CC-', 'rb') as input_file, open('CC-' + file_name, 'wb') as output_file:
        # Write the IV to the output file
        output_file.write(iv)
        
        # Encrypt and write the content of the input file to the output file
        output_file.write(cipher.encrypt(input_file.read()))

def DES_decrypt(key, file_path):
    # Open the input file for reading and the output file for writing
    with open(file_path, 'rb') as input_file, open('DD-', 'wb') as output_file:
        # Read the IV (first 8 bytes) from the input file
        iv = input_file.read(8)

        # Create a new DES cipher object with the given key, OFB mode, and IV
        cipher = DES.new(key, DES.MODE_OFB, iv)

        # Read and decrypt the ciphertext blocks from the input file
        while True:
            block = input_file.read(8)  # Read the ciphertext block (8 bytes)
            if not block:
                break  # Reached the end of the file

            decrypted_block = cipher.decrypt(block)  # Decrypt the block
            output_file.write(decrypted_block)  # Write the decrypted block to the output file


def text_to_int(text_input):
    # Encode the text input to bytes using ASCII encoding
    byte_str = text_input.encode('ascii')

    # Convert the byte string to an integer
    byte_int = int.from_bytes(byte_str, 'big')

    # Return the integer modulo 256 plus 1
    # Ensures the result is between 1 and 256
    return byte_int % 256 + 1

# ROT47 pass Encrypt 
def rot47_encode(keyword):
    encoded_keyword = ""
    for char in keyword:
        ascii_code = ord(char)
        if 33 <= ascii_code <= 126:
            # Apply the ROT47 transformation to printable ASCII characters
            encoded_ascii_code = (ascii_code - 33 + 47) % 94 + 33
            encoded_keyword += chr(encoded_ascii_code)
        else:
            # Preserve non-printable ASCII characters
            encoded_keyword += char

    return encoded_keyword


def hash_keyword16(keyword):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()

    # Update the hash object with the keyword
    sha256.update(keyword.encode())

    # Get the first 16 bytes of the hash as bytes
    hash_bytes = sha256.digest()[:16]

    return hash_bytes

def hash_keyword8(keyword):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()

    # Update the hash object with the keyword
    sha256.update(keyword.encode())

    # Get the first 8 bytes of the hash as bytes
    hash_bytes = sha256.digest()[:8]

    return hash_bytes

def Remove_file(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Remove the file
        os.remove(file_path)

def get_file():
    # Open a file dialog to select a file
    file_path = filedialog.askopenfilename()

    # Get the file type from the file path
    file_type = os.path.splitext(file_path)[1]

    # Clear the entry field
    entry0.delete(0, tk.END)

    # Insert the selected file path into the entry field
    entry0.insert(0, file_path)

    
#====================GUI========================
root = tk.Tk(className='Encryption Project')
root.geometry("500x450")
root.configure(background='#000000')
frame = tk.Frame(master=root, background='#000000', relief=tk.GROOVE, bd=1)
frame.pack(pady=20, padx=60)

# Label styles
label_style = {'background': '#000000', 'foreground': '#20C20E'}
groove_style = {'relief': tk.GROOVE, 'bd': 1}

# row 0
label2 = tk.Label(master=frame, text="Shhhhhh! It's a secret", font=("", 20), **label_style)
label2.grid(row=0, column=0, columnspan=3, pady=12, padx=10)

# row 1
tk.Label(master=frame, text="File:", **groove_style, **label_style).grid(row=1, column=0, padx=10, sticky="W")
entry0 = tk.Entry(master=frame, foreground='#20C20E', background='#000000', **groove_style)
entry0.grid(row=1, column=1, padx=10, columnspan=2, sticky="W")
tk.Button(master=frame, text="Browse", bg='black', fg='#20C20E', **groove_style, command=get_file).grid(row=1, column=2)

# row 2
tk.Label(frame, text="Choose an option:", **groove_style, **label_style).grid(row=2, column=0, padx=10, sticky="W")
options2 = ["Default", "Custom"]
var1 = tk.StringVar(value=options2[0])
for i, option in enumerate(options2):
   rad1= Radiobutton(
        frame, text=option, value=option, bg='#000000', fg='#20C20E',
        highlightbackground='black', highlightcolor='black', selectcolor='black' ,variable=var1
    ).grid(row=2, column=i+1, padx=10, sticky="W")

# row 3
tk.Label(frame, text="Key:", **groove_style, **label_style).grid(row=3, column=0, padx=10, sticky="W")
entry1 = tk.Entry(master=frame, foreground='#20C20E', background='#000000', **groove_style)
entry1.insert(0, "Hello, World!")
entry1.grid(row=3, column=1, padx=10, columnspan=2, sticky="W")

# row 4
tk.Label(frame, text="Mode:", **groove_style, **label_style).grid(row=4, padx=10, sticky="W")
options3 = ["Encrypt", "Decrypt"]
var2 = tk.StringVar(value=options3[0])
for i, option in enumerate(options3):
    rad2 = Radiobutton(
        frame, text=option, value=option, bg='#000000', fg='#20C20E',
        highlightbackground='black', highlightcolor='black', selectcolor='black', variable=var2
    ).grid(row=4, column=i+1, padx=10, sticky="W")

#row 5
listbox1 = tk.Listbox(master=frame, fg='#20C20E', bg='#000000',relief=tk.GROOVE, bd=1)
listbox1.grid(row=5, column=0,padx = 10,columnspan=2,sticky="W" )
tk.Button(master=frame, text="Execute", bg='black', fg='#20C20E', **groove_style, command=run_code).grid(row=5, column=1)
listbox2 = tk.Listbox(master=frame, fg='#20C20E', bg='#000000',relief=tk.GROOVE, bd=1)
listbox2.grid(row=5, column=2 ,padx = 10,sticky="E")

#row6
def update_progress(progress):
    progress_width = progress * frame.winfo_width() // 10
    progressbar.coords("progress", 0, 0, progress_width, 20)

def set_progress(num):
    if num < 1:
        num = 1
    elif num > 10:
        num = 10
    progress_percent = (num - 1) * 10  # calculate progress percentage
    update_progress(progress_percent / 100)  # update progress bar

progressbar = tk.Canvas(frame,height=20, bg='#000000', highlightthickness=0, relief=tk.GROOVE, bd=1)
progressbar.grid(row=6, column=0,columnspan=3 , sticky="W")
progressbar.create_rectangle(0, 0, 0, 20, fill='#20C20E', width=0, tags="progress")

root.mainloop()

