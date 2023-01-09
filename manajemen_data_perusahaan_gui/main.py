''' PEMBUATAN GUI '''
import csv
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Layout =======================================================================================
root = Tk()
root.configure(background='white')
root.geometry('600x600')
root.title('Data Perusahaan')
root.resizable(False, False)

# Frame Inti
display = Frame(root, background='white')
display.pack(padx=30, pady=10, expand=True, fill='both')

# Bagian Layout ================================================================================
# Frame Judul Atas
layoutAtas = Frame(display, background='white')
layoutAtas.pack()

# Frame Scroll
frameScroll = Frame(display, background='white')
frameScroll.pack()

# Frame Sort
frameSort = Frame(display, background='white')
frameSort.pack(fill="both")

# Frame Input Data
inputData = Frame(display, background='white', border=15, highlightcolor='black', highlightthickness=2)
inputData.pack(fill='both')

# Frame Tombol CRUD
tombolCrud = Frame(display, background='white')
tombolCrud.pack(fill='both')

# Variable Data ================================================================================
NAMA = StringVar()
JENISKEL = StringVar()
JABATAN = StringVar()
KEHADIRAN = StringVar()
DELETEDATA = StringVar()

# Daftar Function ==============================================================================
# Baca File CSV
def readCsv():
    ''' READ + UPDATE CSV '''
    with open('data.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        csvtoList = []
        for data_list in reader:
            csvtoList.append(data_list)
        return csvtoList

# Create Csv
def createCsv(createData):
    ''' CREATE CSV '''
    with open('data.csv', 'a', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        for i in createData:
            write_file.writerow(i)

# Delete Csv
def deleteCsv(remove_data):
    ''' DELETE CSV '''
    # Open File CSV nya
    openCsv = readCsv()

    ''' Remove Data '''
    for dataList in openCsv:
        if remove_data in dataList[0]:  # jika ingin menghapus index ke berapa
            openCsv.remove(dataList)

    # Tulis kembali data selain remove data
    with open('data.csv', 'w', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        for i in openCsv:
            write_file.writerow(i)

# Update Data List Box
def update_data(data = list):
    for i in tree.get_children():
        tree.delete(i)
    count = 0

    # Urutkan berdasarkan jabatan
    data.sort(key=lambda x: x[1])
    for item in data:
        count += 1
        tree.insert("", "end", text=count, values=(item[0], item[1], item[2], item[3]))

# Function Search
def functionSearch(e):
    # Mengambil data dengan .get()
    search = searchBox.get()
    if search == '':
        data = readCsv()
    else:
        data = []
        for item in readCsv():
            if search in item[0]:
                data.append(item)
    # Perbarui data
    update_data(data)

# Function Sort
def sortBy(e):
    # file Csv
    data = readCsv()
    sort_by = menuSort.get()
    dataBaru =[]

    # Kondisi Opsi
    if sort_by == 'A-Z':
        data.sort(key=lambda x: x[0])
        update_data(data)

    elif sort_by == 'Z-A':
        data.sort(key=lambda x: x[0], reverse=True)
        update_data(data)

    elif sort_by == 'Direktur':
        for item in data:
            if item[1] == 'Direktur':
                dataBaru.append(item)
        update_data(dataBaru)

    elif sort_by == 'Manajer':
        for item in data:
            if item[1] == 'Manajer':
                dataBaru.append(item)
        update_data(dataBaru)

    elif sort_by == 'Staff':
        for item in data:
            if item[1] == 'Staff':
                dataBaru.append(item)
        update_data(dataBaru)

    elif sort_by == 'Low To Hight':
        data.sort(key=lambda x : x[3])
        update_data(data)

    elif sort_by == 'Hight To Low':
        data.sort(key=lambda x: x[3], reverse=True)
        update_data(data)

    else:
        update_data(data)

# Function Memilih Jenis Kelamin
def pilihanJenisKel():
    dataKel = entriJenisKel.get()
    data = ''
    if dataKel == 'L':
        data = ('Laki-laki')
    elif dataKel == 'P':
        data = ('Perempuan')
    return data

# Menambahkan data ke list CSV
def create_Data_Csv():
    ambil_Nama = NAMA.get()
    # ambil_Jeniskelamin = JENISKEL.get()
    ambil_Jabatan = JABATAN.get()
    ambil_Kehadiran = KEHADIRAN.get()
    # Memasukan data yang diambil ke dalam list
    listTOCsv = [ambil_Nama, ambil_Jabatan, pilihanJenisKel(), ambil_Kehadiran]
    
    # Baca file CSV dulu
    bacaCsv = readCsv()
    # Menaruh semua data ke dataKosong
    dataKosong = []
    for i in bacaCsv:
        dataKosong.append(i)
    dataKosong.append(listTOCsv)

    # Sorting data menurut jabatan
    dataKosong.sort(key=lambda x: x[1])
    # Masukkan semua data ke CSV dengan menimpa data sebelumnya
    createCsv(dataKosong)
    # Auto Update Bosskuuu
    update_data(readCsv())

# Menghapus data CSV dan menampilkan data nya
def delete_Data_Csv():
    ambil_delete_name = DELETEDATA.get()
    deleteCsv(ambil_delete_name)
    update_data(readCsv())

# Isi Layout Atas ==============================================================================
# Judul
judul = Label(layoutAtas, text='DATA PERUSAHAAN',font=('inter', 15), background='white')
judul.pack(fill='y', pady=15)

# garis lurus
canvas = Canvas(layoutAtas, width=600, height=2, background='white')
canvas.pack(fill='y')

# Garis Bagian Judul
line = canvas.create_line(0, 3, 580, 3, fill="black", width=2)

# Search Box
searchBox = ttk.Entry(layoutAtas)
searchBox.pack(ipadx=15, padx=15, pady=15, anchor=E)

# Autosearch
searchBox.bind("<KeyRelease>", functionSearch)


# Tree View and Frame Scroll ===================================================================
# Melakukan scroll
scrollData = Scrollbar(frameScroll)
scrollData.pack(side=RIGHT, fill=Y)

# Buat Treeview
tree = ttk.Treeview(frameScroll, yscrollcommand=scrollData.set)

# Format panggilan & keluaran
tree["columns"] = ("nama", "jabatan", "jenisKel", "kehadiran")

# Column
tree.column("#0", width=50, minwidth=50, stretch=tk.NO)
tree.column("nama", width=100, minwidth=100, stretch=tk.NO)
tree.column("jabatan", width=100, minwidth=100)
tree.column("jenisKel", width=140, minwidth=140)
tree.column("kehadiran", width=100, minwidth=100)

# Heading
tree.heading("#0", text="    No.", anchor=tk.W)
tree.heading("nama", text="Nama", anchor=tk.W)
tree.heading("jabatan", text="Jabatan", anchor=tk.W)
tree.heading("jenisKel", text="Jenis Kelamin", anchor=tk.W)
tree.heading("kehadiran", text="kehadiran (%)", anchor=tk.W)

# Menampailkan Data Tree
update_data(readCsv())
tree.pack()

# Menampilkan scroll
scrollData.config(command=tree.yview)

# Isi Frame Sort ===============================================================================
# Sorting Data list
menuSort = ttk.Combobox(frameSort, values=[
                        'Sorted by...', 'A-Z', 'Z-A', 'Direktur', 'Manajer', 'Staff', 'Low To Hight', 'Hight To Low'], state='readonly')
menuSort.current(0)
menuSort.config(width=15)
menuSort.pack(padx=15, pady=15, fill='y', side=LEFT)

# Menjalankan fungsi pengurutan data
menuSort.bind("<<ComboboxSelected>>",sortBy)

# Frame Input ==================================================================================
# Input Nama
nama = ttk.Label(inputData, background='white', text='Nama', font=('inter', 10))
nama.grid(row=0, column=0, padx=25, pady=7)

entriNama = ttk.Entry(inputData, textvariable=NAMA)
entriNama.grid(row=0, column=1)

# Input Jenis Kelamin
jenisKel = ttk.Label(inputData, background='white',text='Jenis Kelamin', font=('inter', 10))
jenisKel.grid(row=0, column=2, padx=25)

entriJenisKel = ttk.Combobox(inputData, values=['L', 'P'], state='readonly')
entriJenisKel.grid(row=0, column=3)
entriJenisKel.config(width=17)

# Input Jabatan
jabatan = ttk.Label(inputData, background='white',text='Jabatan', font=('inter', 10))
jabatan.grid(row=1, column=0, pady=7)

entriJabatan = ttk.Entry(inputData, textvariable=JABATAN)
entriJabatan.grid(row=1, column=1)

# Input Kedahiran
kehadiran = Label(inputData, background='white', text='Kehadiran', font=('inter', 10))
kehadiran.grid(row=1, column=2)

entriKehadiran = ttk.Entry(inputData, textvariable=KEHADIRAN)
entriKehadiran.grid(row=1, column=3)

# Tombol CRUD ==================================================================================
# Button Create
button_Create = Button(tombolCrud, text='Create', font=('inter', 9), foreground='white', background='green', activebackground='white',
                       activeforeground='black', borderwidth=1, command=create_Data_Csv)
button_Create.grid(row=0, column=0, ipadx=15, ipady=3,pady=20, padx=10)

# Button Delete
button_Delete = Button(tombolCrud, text='Delete', font=('inter', 9), foreground='white', background='green', activebackground='white',
                       activeforeground='black', borderwidth=1, command=delete_Data_Csv)
button_Delete.grid(row=0, column=1, ipadx=15, ipady=3, pady=20, padx=10, )

# Label Delete Data
deleteLabel = Label(tombolCrud, text='Hapus Nama = ', background='white', font=('inter', 9))
deleteLabel.grid(row=0, column=2)

# Entri Delete data
entriDeleteLabel = ttk.Entry(tombolCrud, textvariable=DELETEDATA)
entriDeleteLabel.grid(row=0, column=3)

root.mainloop()