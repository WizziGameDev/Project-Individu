from tkinter import *
from tkinter import ttk
from multi_function import *

# Function ==========================================================================================================================
# Create Csv
def createCsv(createData):
    ''' UPDATE '''
    with open('data.csv', 'w', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        for i in createData:
            write_file.writerow(i)

# Pilihan Yes or No
def YorN():
    value = comboBayar.get()
    if value == 'Yes':
        return 'Y'
    elif value == 'No':
        return 'N'    

# Update Pembayaran
def updatePembayaran():
    data = readCsv()
    nama = entryNama.get()
    hari = pilihHari.get()

    for dataList in data:
        if nama in dataList:
            if hari == "Senin":
                dataList[1] = YorN()
            elif hari == "Rabu":
                dataList[2] = YorN()
            elif hari == "Rabu":
                dataList[3] = YorN()
            elif hari == "Kamis":
                dataList[4] = YorN()
            elif hari == "Jum'at":
                dataList[5] = YorN()
            elif hari == "Sabtu":
                dataList[6] = YorN()     
        
    createCsv(data)
    jendelaBaru.destroy()

# Destroy Pop Up
def desTroy():
    jendelaBaru.destroy()
                
# Display Pop Up ====================================================================================================================
def popUp():
    global jendelaBaru
    jendelaBaru = Tk()
    jendelaBaru.configure(background='white')
    jendelaBaru.geometry('350x225')
    jendelaBaru.title('Melakukan Pembayaran')
    jendelaBaru.resizable(False, False)

    # Bagian Frame ==================================================================================================================
    FramePopUp = Frame(jendelaBaru, background='white')
    FramePopUp.pack(fill='y')

    FrameInput = Frame(jendelaBaru, background='white')
    FrameInput.pack(fill='y')

    # Bagian Display ================================================================================================================
    # Judul
    labelHeader = Label(FramePopUp, font=('inter', 13),
                        text='Lakukan Pembayaran', background='white')
    labelHeader.pack(pady=7)

    # Line
    canvasPopUp = Canvas(FramePopUp, width=350, height=2, background='white')
    canvasPopUp.pack(fill='y', padx=20)
    linePopUp = canvasPopUp.create_line(0, 3, 330, 3, fill="black", width=2)

    # Bagian Nama
    labelNama = Label(FrameInput, text='Nama', background='white')
    labelNama.grid(row=1, column=0, padx=40, pady=13)

    global entryNama
    entryNama = ttk.Entry(FrameInput, background='red')
    entryNama.grid(row=1, column=1, padx=8)

    # Bagian pilihan hari
    labelHari = Label(FrameInput, text='Hari Pembayaran', background='white')
    labelHari.grid(row=2, column=0)

    global pilihHari
    pilihHari = ttk.Combobox(FrameInput, values=["Hari...", "Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu"], state='readonly')
    pilihHari.current(0)
    pilihHari.config(width=17)
    pilihHari.grid(row=2, column=1)

    # Bagian pilihan Yes Or No
    labelBayar = Label(FrameInput, text="Bayar?", background='white')
    labelBayar.grid(row=3, column=0)

    global comboBayar
    comboBayar = ttk.Combobox(FrameInput, values=["Yes/No", "Yes", "No"], state='readonly')
    comboBayar.current(0)
    comboBayar.config(width=17)
    comboBayar.grid(row=3, column=1, pady=13)

    # Tombol Cancel
    buttonCancel = Button(FrameInput, text='Cancel', font=('roboto', 8), foreground='white', background='green', activebackground='white',
                          activeforeground='black', borderwidth=1, command=desTroy)
    buttonCancel.grid(row=4, column=0, ipadx=20, ipady=2, pady=10)
    
    # Tombol update Data
    buttonUpdate = Button(FrameInput, text='Update', font=('roboto', 8), foreground='white', background='green', activebackground='white',
                         activeforeground='black', borderwidth=1, command=updatePembayaran)
    buttonUpdate.grid(row=4, column=1, ipadx=20, ipady=2)
    
    jendelaBaru.mainloop()