#GUI Imports
import tkinter as tk
from tkinter import Radiobutton, messagebox, filedialog, font, ttk
import os
# DES Imports
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
#Global
file_flag = False
file_path = ''

#AES encrypt & decrypt #Skyf




#DES Encrypt & decrypt #Jaap


# Avoid Option 3
while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass

cipher = DES3.new(key, DES3.MODE_CFB)
plaintext = b'We are no longer the knights who say ni!'
msg = cipher.iv + cipher.encrypt(plaintext)



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

