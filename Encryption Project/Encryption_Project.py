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
#Global
file_flag = False
file_path = ''
file_name = ''
key = b''
iv = b''
size = 2048

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
            listbox2.items.add("File encrypted successfully")
        if var2.get() == "Decrypt":
            update_progress(1)
            file_path = entry0.get()
            update_progress(3)
            file_name = os.path.basename(file_path)
            update_progress(6)
            xor_Decrypt(file_name, text_to_int(entry1.get()))
            update_progress(10)
            listbox2.items.add("File decrypted successfully")


    if var1.get() == "Custom":
        if var2.get() == "Encrypt":
            update_progress(1)
            #print(entry1.get())
            #print(rot47_encode(entry1.get()))
            #print(hash_keyword16(rot47_encode(entry1.get())))
            file_path = entry0.get()
            update_progress(3)
            #print(file_path)
            AES_encrypt(file_path,hash_keyword16(rot47_encode(entry1.get())))
            update_progress(5)
  
            convert_file_16_8()
            update_progress(7)
            file_name = os.path.basename(file_path)
            update_progress(9)
            DES_encrypt(hash_keyword8(rot47_encode(entry1.get())),file_name)
            update_progress(10)
            #Remove_file(file_path)
            listbox1.insert(tk.END,"File encrypted successfully")

        if var2.get() == "Decrypt":
            update_progress(1)
            file_path = entry0.get()
            update_progress(3)
            file_name = os.path.basename(file_path)
            update_progress(5)
            AES_decrypt(file_name,hash_keyword16(rot47_encode(entry1.get())),iv)
            update_progress(7)
            convert_file_8_16()
            update_progress(9)
            DES_decrypt(hash_keyword8(rot47_encode(entry1.get())),file_name)
            update_progress(10)
            listbox2.insert(tk.END,"File decrypted successfully")
  
 #xor
def xoe_Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open("CC-" + filename, "wb")
    file.write(data)
    file.close()
    
def xor_Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()   
    


#AES encrypt & decrypt #Skyf
def AES_encrypt(file_path,key1):
    
    iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])

    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX)
    #print(get_file_bytes)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(get_file_bytes(file_path))
    with open('encfase1.bin', 'wb') as fout:
        fout.write(nonce)
        fout.write(ciphertext)
    #print(ciphertext)

def AES_decrypt(file_path, key1, nonce):
    with open('encfase1.bin', 'rb') as fin:
        nonce = fin.read(16)
        ciphertext = fin.read()
    
    cipher = AES.new(key1, AES.MODE_EAX, nonce)
    
    plaintext = cipher.decrypt(ciphertext)
    with open('DD-'+file_path, 'wb') as fout:
        fout.write(plaintext)

        


def DES_encrypt(key3,file_name):
    cipher = DES.new(key3, DES.MODE_OFB)

    with open('encfase2.bin', 'rb') as input_file, open('CC-' + file_name, 'wb') as output_file:        
        output_file.write(cipher.iv + cipher.encrypt(input_file.read()))
        return 'CC-' + file_name



def DES_decrypt(key3,file_name):
    cipher = DES.new(key3, DES.MODE_OFB)
# Open the input and output files
    with open(file_name, 'rb') as input_file, open('decfase1.bin', 'wb') as output_file:
    # Read the input file in blocks of 8 bytes
     while True:
           block = input_file.read(8)
           if not block:
              break  # Reached end of file
          # Decrypt the block and write it to the output file
           decrypted_block = cipher.decrypt(block)
           output_file.write(decrypted_block)

def text_to_int(text_input):
    byte_str = text_input.encode('ascii')
    byte_int = int.from_bytes(byte_str, 'big')
    return byte_int % 256 + 1

def convert_file_8_16():
    with open('decfase1.bin', 'rb') as input_file, open('decfase2.bin', 'wb') as output_file:
        # Read the input file in blocks of 8 bytes
        while True:
            block = input_file.read(8)
            if not block:
                break  # Reached end of file
            # Repeat the block to create a 16-byte block
            block = block + block
            # Write the 16-byte block to the output file
            output_file.write(block)


            # 8 byte to 16 byte help my asseblief
def convert_file_16_8():
    with open('encfase1.bin', 'rb') as input_file, open('encfase2.bin', 'wb') as output_file:
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

    # Get the first 13 bytes of the hash as bytes
    hash_bytes = sha256.digest()[:16]

    return hash_bytes

#hash 8

def hash_keyword8(keyword):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()

    # Update the hash object with the keyword
    sha256.update(keyword.encode())

    # Get the first 8 bytes of the hash as bytes
    hash_bytes = sha256.digest()[:8]

    return hash_bytes
# locked file 1 pass 2 file #Jaap




#source file delete #Skyf
def Remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        listbox1.insert(tk.END,"File removed successfully")
    else:
        listbox1.insert(tk.END,"File could not be removed")

# integration #Skyf en Jaap

# get file bytes
def get_file_bytes(file_path):
    with open(file_path, 'rb') as input_file:
            file_bytes = input_file.read()
            return file_bytes
#gui #Jaap
def get_file():
    #file_flag = True
    file_path = filedialog.askopenfilename()
    file_type = os.path.splitext(file_path)[1]
   

    entry0.delete(0, tk.END)
    entry0.insert(0, file_path)
    

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


# Cal



root.mainloop()

