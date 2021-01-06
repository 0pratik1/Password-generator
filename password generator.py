# Name: Pratik Nimbalkar
# Project : Password Generator

from tkinter import *
import tkinter as tk
import random, string
import pyperclip as pyperclip
root=Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("YAY - PASSWORD GENERATOR")
w = Label(root, text='PLEASE SELECT SIZE \n CLICK ON GENERATE PASSWORD', font="arial 15 bold")
w.pack()

pass_label = Label(root, text = 'PASSWORD LENGTH', font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 4, to_ = 20 , textvariable = pass_len , width = 15).pack()
pass_str = StringVar()
def Generator():
    password = ''
    for x in range (0,4):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
t=Text(root,height=2,width=15)
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)
Entry(root , textvariable = pass_str).pack()
def Copy_password():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)
tk.mainloop()
