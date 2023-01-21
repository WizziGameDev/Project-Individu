import csv

# Membaca File CSV
def readCsv():
    ''' READ + UPDATE CSV '''
    with open('data.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        csvtoList = []
        for data_list in reader:
            csvtoList.append(data_list)
        return csvtoList

def createCsv(createData):
    ''' CREATE CSV '''
    with open('data.csv', 'w', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        for i in createData:
            write_file.writerow(i)