# importing
from tkinter import *
from PIL import ImageTk
from PIL import Image
import PIL.Image
import sys
from tkinter import font
import csv
import pandas as pd
import smtplib
from tkinter import messagebox
import tempfile
import os
import cv2
import numpy as np
import re
from datetime import datetime

global win
from Admin import *
from Teacher import *

# WINDOW 1
win = Tk()
win.title('Smart_Attendance')
# getting screen width and height of display
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
# setting tkinter window size
win.geometry("%dx%d" % (width, height))

# FRAMES
topframe = Frame(win)
topframe.pack()

# For background Image of login page
image = PIL.Image.open('Images_Used//bg.jpeg')
# create a tkinter-compatible photo image from the PIL image
back_image = ImageTk.PhotoImage(image)
# create a label widget to display the image
label_ = Label(image=back_image)
label_.pack()


# cancel the current window
def x():
    win.destroy()


# checking Password in our excel file
def checker():
    global e1, e2
    username = e1.get()
    password = e2.get()
    check_password(username, password)


# checking Password
def check_password(u, p):
    import csv
    from tkinter import messagebox
    with open("CSV_files//users_passwords.csv", 'r') as f:
        x = csv.reader(f)
        temp = 1
        for i in x:
            for j in range(1):
                if (u == 'Admin' and p == '12345'):
                    win.destroy()  # current page destroy
                    window2()
                    temp = 0
                    break
                else:
                    if (i[j] == u and i[j + 1] == p):
                        win.destroy()
                        window3()
                        temp = 0
                        break
                    elif (u == '' and p == ''):
                        temp = 2
        if (temp != 0 and temp != 2):
            msg = messagebox.showinfo("message", 'Sorry incorrect Username or password')
        if (temp == 2):
            msg = messagebox.showinfo("message", 'Please Enter username and password')


myFont = font.Font(size=25)
# For button
# b1_image = PhotoImage(file="Images_Used//login.png")
# b1 = Button(image=b1_image,cursor="circle",command=checker)
b1 = Button(text='     Login     ', bg='black', fg='white', height=1, width=10, command=checker, cursor="circle")
b1['font'] = myFont
b1.place(x=500, y=550)
# b2_image = PhotoImage(file="Images_Used//cancel.png")
# b2 = Button(image=b2_image,cursor="circle",command=x)
b2 = Button(text='     Cancel     ', bg='black', fg='white', height=1, width=10, command=x, cursor="circle")
b2['font'] = myFont
b2.place(x=810, y=550)

# For Entry box
e1 = Entry(win, bd=5, fg="magenta4", relief=GROOVE, width=20, font=('Arial 20'))
e1.place(x=710, y=348)
e2 = Entry(win, bd=5, fg="magenta4", show="*", relief=GROOVE, width=20, font=('Arial 20'))
e2.place(x=710, y=448)

# For text box
font_1 = font.Font(family='helvetica', size=20, weight="bold")
label_1 = Label(win, text='USERNAME :', fg="blue")
label_1['font'] = font_1
label_2 = Label(win, text="PASSWORD :", fg="blue")
label_2['font'] = font_1
label_1.place(x=510, y=350)
label_2.place(x=510, y=450)

win.mainloop()
