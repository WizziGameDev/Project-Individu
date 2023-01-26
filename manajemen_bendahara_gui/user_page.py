import tkinter as tk
from tkinter import *
from tkinter import ttk
from multi_function import *

# Display
user_root = Tk()
user_root.configure(background='white')
user_root.geometry('600x415')
user_root.title('user')
user_root.resizable(False, False)

nameFIleCsv = 'data.csv'

# Frame Pembungkus ==================================================================================================================
display = Frame(user_root, background='white')
display.pack(padx=30, pady=10, expand=True, fill='both')

# Frame Judul
FrameHeader = Frame(display, background='white')
FrameHeader.pack()

# Frame Action
FrameAction = Frame(display, background='white')
FrameAction.pack(fill='x')

# Frame Data
FrameData = Frame(display, background='white')
FrameData.pack()

# Frame Button
FrameButton = Frame(display, background='white')
FrameButton.pack(fill='both')

# Bagian Function ===================================================================================================================
# Update Data List Box


def update_data(data=list):
    for i in tree.get_children():
        tree.delete(i)

    count = 0
    for item in data:
        count += 1
        tree.insert("", "end", text=count, values=(
            item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

# Fungsi Search


def functionSearch(e):
    # Mengambil data dengan .get()
    search = searchBox.get()
    if search == '':
        data = readCsv(nameFIleCsv)
    else:
        data = []
        for item in readCsv(nameFIleCsv):
            if search in item[0]:
                data.append(item)
    # Perbarui data
    update_data(data)

# Function Sort

def sortBy(e):
    # file Csv
    data = readCsv(nameFIleCsv)
    sort_by = sortedBy.get()

    # Kondisi Opsi
    if sort_by == 'A-Z':
        data.sort(key=lambda x: x[0])

    elif sort_by == 'Z-A':
        data.sort(key=lambda x: x[0], reverse=True)

    update_data(data)


def buttonUpdate():
    update_data(readCsv(nameFIleCsv))


def buttonLogOut():
    user_root.destroy()
    import login_page

# Bagian Tampilan ===================================================================================================================
judul = Label(FrameHeader, text='DATA BENDAHARA',
              font=('inter', 15), background='white')
judul.pack(fill='y', pady=15)

# garis lurus
canvas = Canvas(FrameHeader, width=600, height=2, background='white')
canvas.pack(fill='y')

# Garis Bagian Judul
line = canvas.create_line(0, 3, 580, 3, fill="black", width=2)

# Bagian Filter =====================================================================================================================
# Search Box
searchBox = ttk.Entry(FrameAction)
searchBox.grid(ipadx=15, padx=10, pady=10, row=0, column=0)

# Autosearch
searchBox.bind("<KeyRelease>", functionSearch)

# Sorted
sortedBy = ttk.Combobox(
    FrameAction, values=['Sorted by...', 'A-Z', 'Z-A'], state='readonly')
sortedBy.current(0)
sortedBy.config(width=10)
sortedBy.grid(padx=270, row=0, column=1)

# Menjalankan fungsi pengurutan data
sortedBy.bind("<<ComboboxSelected>>", sortBy)

# Tree View and Frame Scroll ========================================================================================================
# Melakukan scroll
scrollData = Scrollbar(FrameData)
scrollData.pack(side=RIGHT, fill=Y)

# Buat Treeview
tree = ttk.Treeview(FrameData, yscrollcommand=scrollData.set)

# Format panggilan & keluaran
tree["columns"] = ("nama", "senin", "selasa",
                   "rabu", "kamis", "jumat", "sabtu")

# Column
tree.column("#0", width=50, minwidth=50, stretch=tk.NO)
tree.column("nama", width=150, minwidth=150, stretch=tk.NO)
tree.column("senin", width=50, minwidth=50)
tree.column("selasa", width=50, minwidth=50)
tree.column("rabu", width=50, minwidth=50)
tree.column("kamis", width=50, minwidth=50)
tree.column("jumat", width=50, minwidth=50)
tree.column("sabtu", width=50, minwidth=50)

# Heading
tree.heading("#0", text="    No.", anchor=tk.W)
tree.heading("nama", text="Nama", anchor=tk.W)
tree.heading("senin", text="Senin", anchor=tk.W)
tree.heading("selasa", text="Selasa", anchor=tk.W)
tree.heading("rabu", text="Rabu", anchor=tk.W)
tree.heading("kamis", text="Kamis", anchor=tk.W)
tree.heading("jumat", text="Jum'at", anchor=tk.W)
tree.heading("sabtu", text="Sabtu", anchor=tk.W)

# Menampailkan Data Tree
update_data(readCsv(nameFIleCsv))
tree.pack()

# Menampilkan scroll
scrollData.config(command=tree.yview)

buttonBayar = Button(FrameButton, text='UPDATE', font=('roboto', 9), foreground='white', background='green', activebackground='white',
                     activeforeground='black', borderwidth=0, cursor='hand2', command=buttonUpdate)
buttonBayar.grid(row=0, column=0, ipadx=30, ipady=3, pady=20, padx=10)

buttonBayar = Button(FrameButton, text='LOG OUT', font=('roboto', 9), foreground='white', background='red', activebackground='white',
                     activeforeground='black', borderwidth=0, cursor='hand2', command=buttonLogOut)
buttonBayar.grid(row=0, column=1, ipadx=27, ipady=3, pady=20, padx=10)

user_root.mainloop()