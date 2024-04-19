""" Digital Clock by Kevin Leon Smith 8.23.23 """

import tkinter as tk
from time import strftime

def update_time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock by KLS")
root.geometry("300x150")
root.configure(bg="black")

label = tk.Label(root, font=('Helvetica', 36), bg='black', fg='white')
label.pack(expand=True)

update_time()

root.mainloop()

