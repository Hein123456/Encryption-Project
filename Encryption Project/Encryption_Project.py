#GUI Imports
from asyncio.windows_events import NULL
from msilib.schema import RadioButton
import tkinter as tk
from tkinter import Radiobutton, Variable, messagebox, filedialog, font, ttk
import os
import random

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
            #print(entry1.get())
            #print(rot47_encode(entry1.get()))
            #print(hash_keyword16(rot47_encode(entry1.get())))
            file_path = entry0.get()
            file_name = os.path.basename(file_path)
            update_progress(3)
            #print(file_path)
             
            encrypt_file(file_name, 'output1.bin',convert_key(entry1.get(),32))
            update_progress(7)
            
            #convert_file_16_8(file_name)
            update_progress(9)
            update_progress(10)
            #Remove_file(file_path)
            listbox1.insert(tk.END,"File encrypted successfully")

        if var2.get() == "Decrypt":
            update_progress(1)
            file_path = entry0.get()
            update_progress(3)
            file_name = os.path.basename(file_path)
            update_progress(5)
            #convert_file_8_16(file_name)
            decrypt_file('output1.bin',file_name , convert_key(entry1.get(),32))
            
            update_progress(7)
            #convert_file_16_8(file_name)
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
    






def Remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        listbox1.insert(tk.END,"File removed successfully")
    else:
        listbox1.insert(tk.END,"File could not be removed")



#gui #Jaap
def get_file():
    #file_flag = True
    file_path = filedialog.askopenfilename()
    file_type = os.path.splitext(file_path)[1]
   

    entry0.delete(0, tk.END)
    entry0.insert(0, file_path)

 # GUI ========================================================

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

