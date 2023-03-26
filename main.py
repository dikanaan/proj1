import os
print('MENU DATA')
print('[1] Semua Data')
print('[2] Cari Data (NIK)')
mode = input('Masukan Pilihan : ')
if mode == '1':
    os.system('python data.py')
elif mode == '2':
    print(' Mantenance ')