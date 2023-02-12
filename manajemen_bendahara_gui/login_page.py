from tkinter import messagebox 
from tkinter import *
from tkinter import ttk
from multi_function import *

def funcLoginPage():
    login_root = Tk()
    login_root.geometry('500x415')
    login_root.resizable(False, False)
    login_root.configure(background='Grey')
    login_root.title('login')

    # Text Variable
    USERNAME = StringVar()
    PASSWORD = StringVar()
    
    global count
    count = 2
    nameFIleCsv = 'data_akun.csv' # Csv Data Akun
    
    # Function untuk masuk ke page selanjutnya
    def actionLogin():
        global count
        data_akun = readCsv(nameFIleCsv)
        username = USERNAME.get()
        password = PASSWORD.get()
        found = False

        if username != '' and password != '':
            if username == 'admin' and int(password) == 123:
                toAdmin()
            else:
                for data in data_akun:
                    if username == data[0] and password == data[1]:
                        toUser()
                        found = True

                if not found:
                    messagebox.showwarning('warning', f'Incorrect username and password, remaining {count} times')
                    if count > 0:
                        count -= 1
                    else:
                        messagebox.showinfo('time out', f'Your login time out, you can come back later. Thank you')
                        login_root.destroy()
        else:
            messagebox.showerror('error','Username and password have not been filled in !!!')

    def toSign():
        login_root.destroy()
        from signup_page import funcSignUpPage
        funcSignUpPage()

    def toAdmin():
        login_root.destroy()
        from admin_page import funcAdminPage
        funcAdminPage()

    def toUser():
        login_root.destroy()
        from user_page import funcUserPage
        funcUserPage()

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

funcLoginPage()
