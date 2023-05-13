#GUI Imports
import tkinter as tk
from tkinter import Radiobutton, messagebox, filedialog, font, ttk
import os
import random
# DES Imports
from Crypto.Cipher import DES
# AES Imports
from Crypto.Cipher import AES
#Global
file_flag = False
file_path = ''
file_name = ''
key = ""
iv = ""

#AES encrypt & decrypt #Skyf
def AES_encrypt():
    key = "Working progress"
    iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])
    size = 2048

    aes = AES.new(key, AES.MODE_CBC, iv)

    fsize = os.path.getsize(file_name)

    with open('output.bin', 'wb') as fout:
        fout.write(struct.pack('<Q', fsize))

    with open(file_name, 'rb') as fin:
        while True:
            data = fin.read(size)
            n = len(data)
            if n == 0:
                break
            elif n % 16 != 0:
                data += ' ' * (16 - n % 16)
            encoded = aes.encrypt(data)
            fout.write(encoded)

    
#jou poes


    



#DES Encrypt & decrypt #Jaap




# Set the key and initialization vector (IV)
key = b'secretkey toets 123'
iv = b'12345678'

# Create a DES cipher object with the key and IV
cipher = DES.new(key, DES.MODE_CBC, iv)

# Open the input and output files
with open('input.bin', 'rb') as input_file, open('output.bin', 'wb') as output_file:
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



# ROT47 pass Encrypt #Skyf


# locked file 1 pass 2 file #Jaap



#source file delete #Skyf


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

options2 = ["Option 1", "Option 2"]
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

listbox2 = tk.Listbox(master=frame, fg='#20C20E', bg='#000000',relief=tk.GROOVE, bd=1)
listbox2.grid(row=5, column=2 ,padx = 10,sticky="E")

#row 6 
def update_progress(progress):
    progress_width = progress * frame.winfo_width() // 10
    progressbar.coords("progress", 0, 0, progress_width, 20)
    if progress < 10:
        root.after(100, update_progress, progress + 1)

# add progress bar
progressbar = tk.Canvas(frame,height=20, bg='#000000', highlightthickness=0, relief=tk.GROOVE, bd=1)
progressbar.grid(row=6, column=0,columnspan=3 , sticky="W")

progressbar.create_rectangle(0, 0, 0, 20, fill='#20C20E', width=0, tags="progress")

# start progress
update_progress(1)

root.mainloop()

