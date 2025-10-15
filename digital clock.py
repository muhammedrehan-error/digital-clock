import tkinter as tk
from time import strftime

root=tk.Tk()
root.title("Digital Clock")

def time():
    string=strftime("%I:%M:%S %p \n %D")
    label.config(text=string)
    label.after(50, time)

label=tk.Label(root,font=('arial',50,'bold'),background='green',foreground='black')
label.pack(anchor='center')

time()
root.mainloop()
