from tkinter import *
from tkinter import ttk
from multi_function import *

nameFIleCsv = 'data.csv'

# Bagian Function ===============================================================================================================
# Destroy Pop Up
def desTroy():
    root_cd.destroy()

# Fungsi Delete
def functionDelete():
    nama = entryCD.get()

    if nama != '':
        dataCsv = readCsv(nameFIleCsv)
        for data in dataCsv:
            if nama in data[0]:
                dataCsv.remove(data)
        createCsv(dataCsv)
    else:
        pass

# Fungsi Create
def functionCreate():
    nama = entryCD.get()

    if nama != '':
        dataList = [nama, 'N','N','N','N','N','N']
        addData = []

        dataCsv = readCsv(nameFIleCsv)
        for data in dataCsv:
            addData.append(data)
        addData.append(dataList)

        createCsv(addData)    
    else:
        pass

def creDel():
    global root_cd
    root_cd = Tk()
    root_cd.configure(background='white')
    root_cd.geometry('350x150')
    root_cd.title('Melakukan Pembayaran')
    root_cd.resizable(False, False)

    # Bagian Frame ==================================================================================================================
    FrameHeader = Frame(root_cd, background='white')
    FrameHeader.pack(fill='y')

    FrameInput = Frame(root_cd, background='white')
    FrameInput.pack(fill='y')

    FrameButton = Frame(root_cd, background='white')
    FrameButton.pack(fill='y')

    # Bagian Display ================================================================================================================
    # Judul CD
    judulCD = Label(FrameHeader, text='CREATE AND DELETE', font=('inter', 13), background='white')
    judulCD.pack(pady=7)

    # Line
    canvasCD = Canvas(FrameHeader, width=350, height=2, background='white')
    canvasCD.pack(fill='y', padx=20)
    lineCD = canvasCD.create_line(0, 3, 330, 3, fill="black", width=2)

    # Label Nama
    nameCD = Label(FrameInput, text='Nama', background='white')
    nameCD.grid(row=0, column=0, padx=20, pady=18)
    
    global entryCD
    entryCD = ttk.Entry(FrameInput)
    entryCD.grid(row=0, column=1)

    # Tombol Cancel
    buttonCancel = Button(FrameButton, text='Cancel', font=('roboto', 8), foreground='white', background='grey', activebackground='white',
                          activeforeground='black', borderwidth=0, cursor='hand2', command=desTroy)
    buttonCancel.grid(row=1, column=0, ipadx=10, ipady=2)

    # Tombol Delete Data
    buttonDelete = Button(FrameButton, text='Delete', font=('roboto', 8), foreground='white', background='red', activebackground='white',
                          activeforeground='black', borderwidth=0, cursor='hand2', command=functionDelete)
    buttonDelete.grid(row=1, column=1, ipadx=10, ipady=2, padx=25)

    # Tombol Create Data
    buttonCreate = Button(FrameButton, text='Create', font=('roboto', 8), foreground='white', background='green', activebackground='white',
                          activeforeground='black', borderwidth=0, cursor='hand2', command=functionCreate)
    buttonCreate.grid(row=1, column=2, ipadx=10, ipady=2)
    
    root_cd.mainloop()