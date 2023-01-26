import tkinter as tk
from tkinter import *
from tkinter import ttk
from multi_function import *

login_root = Tk()
login_root.geometry('500x415')
login_root.resizable(False, False)
login_root.configure(background='Grey')
login_root.title('login')

# Text Variable
USERNAME = StringVar()
PASSWORD = StringVar()

nameFIleCsv = 'data_akun.csv'

# Fungsi untuk mengolah data
def actionLogin():
    data_akun = readCsv(nameFIleCsv)
    username = USERNAME.get()
    password = PASSWORD.get()
    number = 0
    print(number)

    while number < 3:
        if username == 'dia':
            pass
        else:
            number += 1
    # if username != '' and password != '':
    #     if username == 'admin' and int(password) == 123:
    #         toAdmin()
    #     else:
    #         for data in data_akun:
    #             if username == data[0] and password == data[1]:
    #                 toUser()
    #             else:
    #                 pass
    # else:
    #     pass

def toSign():
    login_root.destroy()
    import signup_page

def toAdmin():
    login_root.destroy()
    import main

def toUser():
    login_root.destroy()
    import user_page

# Display semua komponen login
rootDisplay = ttk.Frame(login_root)
rootDisplay.pack(padx=50, pady=60, expand=True, fill='both')

app = ttk.Frame(rootDisplay)
app.pack(fill='both')

buttonFrame = ttk.Frame(rootDisplay)
buttonFrame.pack()

title = ttk.Label(app, font=('Roboto', 20), text='LOGIN SYSTEM')
title.pack(pady=20, fill='y')

usernameTitle = ttk.Label(app, font=('Roboto', 10), text='Username')
usernameTitle.pack(padx=40, pady=7, fill='x')

usernameInput = ttk.Entry(app, textvariable=USERNAME)
usernameInput.pack(padx=40, pady=0, fill='x')

passwordTitle = ttk.Label(app, font=('Roboto', 10), text='Password')
passwordTitle.pack(padx=40, pady=7, fill='x')

passwordInput = ttk.Entry(app, textvariable=PASSWORD)
passwordInput.pack(padx=40, pady=0, fill='x')

signButton = Button(buttonFrame, text='Sign Up', activebackground='grey',
                    background='green', width=10, height=1, border='0', font=('Roboto', 10), foreground='white', command=toSign, cursor='hand2')
signButton.grid(row=0, column=0, padx=30, ipadx=3, ipady=2)

loginButton = Button(buttonFrame, text='Log in', activebackground='grey',
                        background='green', width=10, height=1, border='0', font=('Roboto', 10), foreground='white', command=actionLogin, cursor='hand2')
loginButton.grid(row=0, column=1, padx=30, pady=35, ipadx=3, ipady=2)

# Looping
login_root.mainloop()