import tkinter as tk
from tkinter import *
from tkinter import ttk
from multi_function import *

# Sign ==================================================================================================================================
# Display apps
global sign_root
sign_root = Tk()
sign_root.configure(background='grey')
sign_root.geometry('500x415')
sign_root.resizable(False, False)
sign_root.title('Sign Up System')

# Variabel Pendukung
USERNAME = StringVar()
PASSWORD = StringVar()
CHECKBUTTON = IntVar()

# Fungsi
def actionSignup():
    username = USERNAME.get()
    password = PASSWORD.get()
    buttonCheck = CHECKBUTTON.get()

    if username != '' and int(password) != int() and buttonCheck == 1:
        writeCsv = [username, int(password)]
        createCsvNewLine(writeCsv, 'data_akun.csv')
    else:
        pass
    backPage()

def backPage():
    sign_root.destroy()
    import login_page

# Frame
rootDisplay = tk.Frame(sign_root)
rootDisplay.pack(padx=50, pady=60, expand=True, fill='both')

sign = tk.Frame(rootDisplay)
sign.pack(fill='both')

buttonFrame = ttk.Frame(rootDisplay)
buttonFrame.pack()

# Label Sign Up
judul = ttk.Label(sign, text='CREATE AN ACCOUNT', font=('Roboto', 20))
judul.pack(pady=20, fill='y')

# Entry Username
UsernameLabel = ttk.Label(sign, text='Username', font=('Roboto', 10))
UsernameLabel.pack(padx=40, pady=7, fill='x')

UsernameEntry = ttk.Entry(sign, textvariable=USERNAME)
UsernameEntry.pack(padx=40, pady=0, fill='x')

# Entry Password
PasswordLabel = ttk.Label(sign, text='Password', font=('Roboto', 10))
PasswordLabel.pack(padx=40, pady=7, fill='x')

PasswordEntry = ttk.Entry(sign, textvariable=PASSWORD)
PasswordEntry.pack(padx=40, pady=0, fill='x')

checkBox = Checkbutton(sign, onvalue=1, offvalue=0, text='condition and tems', font=(
    'Roboto', 8), variable=CHECKBUTTON)
checkBox.pack(pady=15, fill='x')

logInButton = Button(buttonFrame, text='Cancel', command=backPage, activebackground='grey',
                        background='grey', width=10, height=1, border=0, font=('Roboto', 10), foreground='white')
logInButton.grid(row=0, column=0, padx=30, pady=0, ipadx=3, ipady=2)

signUpButton = Button(buttonFrame, text='Sign Up', command=actionSignup, activebackground='grey',
                        background='green', width=10, height=0, border=0, font=('Roboto', 10), foreground='white')
signUpButton.grid(row=0, column=1, padx=30, ipadx=3, ipady=2)

sign_root.mainloop()
