import pandas

data = pandas.read_excel('data.xlsx')
dnama = data['Nama']
dnik = data['Nik']

count = 0
while(count < len(dnik)):
    print ('Nama : '+ dnama[count] + ' ( '+str(int(dnik[count]))+')')
    count = count + 1