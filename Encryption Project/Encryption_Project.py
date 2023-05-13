#GUI Imports
import tkinter as tk
from tkinter import Radiobutton, messagebox, filedialog, font, ttk
import os
import random
# DES Imports
from Crypto.Cipher import DES
# AES Imports
from Crypto.Cipher import AES
#hash
import hashlib
#Global
file_flag = False
file_path = ''
file_name = ''
key = ""
iv = ""
size = 2048
int i = 0
#main
def run_code():
    print("yes")
    # start progress
    set_progress(i) 
    i = i+1

#AES encrypt & decrypt #Skyf
def AES_encrypt():
    key = "Working progress"
    iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])

    aes = AES.new(key, AES.MODE_CBC, iv)

    fsize = os.path.getsize(file_path)

    with open(file_path, 'rb') as fin, open('output.bin', 'wb') as fout:
        while True:
            data = fin.read(size)
            n = len(data)
            if n == 0:
                break
            elif n % 16 != 0:
                data += ' ' * (16 - n % 16)
            encoded = aes.encrypt(data)
            fout.write(encoded)

def AES_decrypt():
    with open(file_name + '.enc', rb) as fin:
        fsize = struct.unpack('<Q', fin.read(struct.calcsize('<Q')))[0]
        iv = fin.read(16)

    aes = AES.new(key, AES.MODE_CBC, iv)

    with open('phase1.bin', 'wb') as fout:
        while True:
            data = fin.read(size)
            if n == 0:
                break
            decode = aes.decrypt(data)
            n = len(data)
            if fsize > n:
                fout.write(decode)
            else:
                fout.write(decode[:fsize])

            fsize -= n
        


def DES_encrypt():


# Create a DES cipher object with the key and IV
    cipher = DES.new(key, DES.MODE_CBC, iv)

# Open the input and output files
    with open('output.bin', 'wb') as output_file:
    # Read the input file in blocks of 8 bytes
        while True:
            block = input_file.read(8)
            if not block:
                break  # Reached end of file
        # Pad the block if necessary
            if len(block) < 8:
                block += b'\0' * (8 - len(block))
        # Encrypt the block and write it to the output file
            encrypted_block = cipher.encrypt(block)
            output_file.write(encrypted_block)

def DES_decrypt():
# Open the input and output files
   with open('decrypted_output.bin', 'wb') as output_file:
    # Read the input file in blocks of 8 bytes
     while True:
           block = file_path.read(8)
           if not block:
              break  # Reached end of file
          # Decrypt the block and write it to the output file
           decrypted_block = DES.decrypt(block)
           output_file.write(decrypted_block)

            # 8 byte to 16 byte help my asseblief
def convert_file():
    with open('input_file.bin', 'rb') as input_file, open('output_file.bin', 'wb') as output_file:
    # Read the input file in blocks of 16 bytes
      while True:
        block = input_file.read(16)
        if not block:
            break  # Reached end of file
         # Split the block into two 8-byte blocks
        block1 = block[:8]
        block2 = block[8:]
        # Write the two blocks to the output file
        output_file.write(block1)
        output_file.write(block2)
# ROT47 pass Encrypt #Skyf
def rot47_encode(keyword):
    encoded_keyword = ""
    for char in keyword:
        ascii_code = ord(char)
        if 33 <= ascii_code <= 126:
            encoded_ascii_code = (ascii_code - 33 + 47) % 94 + 33
            encoded_keyword += chr(encoded_ascii_code)
        else:
            encoded_keyword += char
    return encoded_keyword


def decode_rot47(keyword):
   # """Decode a keyword using ROT47 encryption"""
    # Initialize an empty result string
    result = ""

    # Loop through each character in the keyword
    for c in keyword:
        # Get the ASCII code of the character
        ascii_code = ord(c)

        # If the character is in the range of printable ASCII characters
        if 33 <= ascii_code <= 126:
            # Decode the character using the ROT47 algorithm
            decoded_char = chr(33 + ((ascii_code + 14) % 94))
        else:
            # Otherwise, the character is not in the range of printable ASCII characters,
            # so just append it as is to the result string
            decoded_char = c
        
        # Append the decoded character to the result string
        result += decoded_char
    
    # Return the decoded result
    return result

#hash 16
def hash_keyword16(keyword):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()


    # Update the hash object with the keyword
    sha256.update(keyword.encode())

    # Get the first 16 bytes of the hash as bytes
    hash_bytes = sha256.digest()[:16]

    # Convert the bytes to a hex string
    hash_hex = hash_bytes.hex()

    return hash_hex
#hash 8

def hash_keyword8(keyword):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()

    # Update the hash object with the keyword
    sha256.update(keyword.encode())

    # Get the first 8 bytes of the hash as bytes
    hash_bytes = sha256.digest()[:8]

    # Convert the bytes to a hex string
    hash_hex = hash_bytes.hex()

    return hash_hex
# locked file 1 pass 2 file #Jaap




#source file delete #Skyf
def Remove_file():
    if os.path.exists(file_path):
        os.remove(file_path)
        print("The file has been deleted successfully")
    else:
        print("The file does not exists!")

# integration #Skyf en Jaap

# get file bytes
def get_file_bytes():
    if file_flag:
        with open(file_path, 'rb') as input_file:
            file_bytes = input_file.read()
        return file_bytes
    else:
        #print("File flag is False. The script will now exit.")
        exit()  # stop the script
#gui #Jaap
def get_file():
    file_flag = True
    file_path = filedialog.askopenfilename()
    file_type = os.path.splitext(file_path)[1]
    file_name = os.path.basename(file_path)

    entry0.delete(0, tk.END)
    entry0.insert(0, file_name)

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
var = tk.StringVar(value=options2[0])

for i, option in enumerate(options2):
    Radiobutton(
        frame, text=option, variable=var, value=option, bg='#000000', fg='#20C20E',
        highlightbackground='black', highlightcolor='black', selectcolor='black'
    ).grid(row=2, column=i+1, padx=10, sticky="W")

# row 3
tk.Label(frame, text="Key:", **groove_style, **label_style).grid(row=3, column=0, padx=10, sticky="W")
entry1 = tk.Entry(master=frame, foreground='#20C20E', background='#000000', **groove_style)
entry1.grid(row=3, column=1, padx=10, columnspan=2, sticky="W")

# row 4
tk.Label(frame, text="Mode:", **groove_style, **label_style).grid(row=4, padx=10, sticky="W")

options3 = ["Encrypt", "Decrypt"]
var = tk.StringVar(value=options3[0])

for i, option in enumerate(options3):
    Radiobutton(
        frame, text=option, variable=var, value=option, bg='#000000', fg='#20C20E',
        highlightbackground='black', highlightcolor='black', selectcolor='black'
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
    progress = (num - 1) / 9  # scale the number between 0 and 1
    update_progress(progress)
progressbar = tk.Canvas(frame,height=20, bg='#000000', highlightthickness=0, relief=tk.GROOVE, bd=1)
progressbar.grid(row=6, column=0,columnspan=3 , sticky="W")

progressbar.create_rectangle(0, 0, 0, 20, fill='#20C20E', width=0, tags="progress")


# Cal



root.mainloop()

