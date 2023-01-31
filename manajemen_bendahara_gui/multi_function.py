import csv

# Membaca File CSV
def readCsv(dataFileCsv):
    ''' READ + UPDATE CSV '''
    with open(dataFileCsv) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        csvtoList = []
        for data_list in reader:
            csvtoList.append(data_list)
        return csvtoList

def createCsv(createData, namefileCsv):
    ''' CREATE CSV '''
    with open(namefileCsv, 'w', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        for i in createData:
            write_file.writerow(i)

def createCsvNewLine(createData, namefileCsv):
    ''' CREATE '''
    with open(namefileCsv, 'a', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        write_file.writerow(createData)
