
import tkinter as tk # dont remove
from tkinter import Radiobutton, messagebox, filedialog, filedialog ,font,ttk# dont remove
import os  # dont remove
# algorithms =============================================================================================





# get file
def get_file():
    file_path = filedialog.askopenfilename() # open dialog for file input 
    file_type = os.path.splitext(file_path)[1] # extract file ectention
    file_name = os.path.basename(file_path) # extract file name

    
    entry0.delete(0, tk.END)  # Clear the current text
    entry0.insert(0, file_name)  # Insert the new text
    
 
    #print("Selected file path:", file_path)


#GUI============================================================================================== 

root = tk.Tk(className='Encryption Project')

root.geometry("500x450")
root.configure(background='#000000')

frame = tk.Frame(master=root, background='#000000', relief=tk.GROOVE, bd=1)
frame.pack(pady=20, padx=60)

#row 0
label2 = tk.Label(master=frame, text="Shhhhhh! It's a secret", background='#000000', foreground='#20C20E', font=("", 20))
label2.grid(row=0, column=0 ,columnspan=3, pady=12, padx=10 ) 


# row 1
label = tk.Label(master=frame, text="File:", relief=tk.GROOVE, bd=1, background='#000000', foreground='#20C20E')
label.grid(row=1, column=0,padx = 10,sticky="W")

entry0 = tk.Entry(master=frame, text='Select a File', foreground='#20C20E', background='#000000',relief=tk.GROOVE, bd=1)
entry0.grid(row=1, column=1 ,padx = 10,columnspan=2 , sticky="W")

button = tk.Button(master=frame, text="Browse", bg='black', fg='#20C20E', relief=tk.GROOVE, bd=1, command=get_file)
button.grid(row=1, column=2 )

#row 2
label = tk.Label(frame, text="Choose an option:",relief=tk.GROOVE, bd=1, foreground='#20C20E', background='#000000')
label.grid(row=2, column=0 ,padx = 10, sticky="W")

options2 = ["Option 1", "Option 2"]
var = tk.StringVar()
var.set(options2[0])

for i, option in enumerate(options2):
    radio_button = Radiobutton(frame, text=option, variable=var, value=option,bg='#000000', fg = '#20C20E' ,highlightbackground = 'black',highlightcolor ='black' , selectcolor ='black' )

    radio_button.grid(row=2, column=i+1 ,padx = 10, sticky="W")

#row 3
label = tk.Label(frame, text="Key:", relief=tk.GROOVE, bd=1, foreground='#20C20E', background='#000000')
label.grid(row=3, column=0 , padx = 10,sticky="W")

entry1 = tk.Entry(master=frame, text='key', foreground='#20C20E', background='#000000',relief=tk.GROOVE, bd=1)
entry1.grid(row=3, column=1 ,padx = 10,columnspan=2 , sticky="W")

#row 4

options3 = ["Encrypt", "Decrypt"]
var = tk.StringVar()
var.set(options3[0])

for i, option in enumerate(options3):
    radio_button = Radiobutton(frame, text=option, variable=var, value=option ,bg='#000000', fg = '#20C20E',highlightbackground = 'black',highlightcolor ='black' , selectcolor ='black')
    radio_button.grid(row=4, padx = 10,column=i+1 , sticky="W")
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

