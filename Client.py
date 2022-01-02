import xmlrpc.client
import time

server = xmlrpc.client.ServerProxy("http://103.171.85.200:81")

exit = False

print('Selamat Datang pad Program Pelaporan Covid-19')

def input_nik(message): # prosedur pengecekan input berupa angka pada input NIK
  while True:
    try:
       input_user = int(input(message))       
    except ValueError:
       print("Mohon Input NIK Berupa Angka!!!")
       continue
    else:
       return str(input_user) 
       break

def input_check(massage): # prosedur pengecekan input ya/tidak
   while True:
      input_user = input(massage).lower()

      if input_user == 'ya' or input_user == 'tidak':
         return input_user
         break


while not exit:
    print('Silahkan Mengisi Data Berikut')

    nama_pelapor = input('Nama Pelapor  : ') # Input Nama Pelapor
    nama_pelapor = nama_pelapor.title()

    nik = input_nik('NIK Pelapor    : ') # Input NIK Pelapor

    nama_terduga = input('Nama Terduga Covid-19 : ') # Input Nama terduga covid
    nama_terduga = nama_terduga.title()

    gejala = input('Gejala yang Timbul  : ')# Input gejala terduga covid
    gejala = gejala.capitalize()

    alamat_terduga = input('Alamat Terduga Covid-19 : ') # Input alamat terduga covid 19
    alamat_terduga = alamat_terduga.capitalize()

    res = server.lapor(nik,nama_pelapor,nama_terduga,gejala,alamat_terduga) # mengirim data ke server
    print(res)
    
    input_kembali = input_check("Input Data Kembali? (ya/tidak)")
    
    if input_kembali.lower() == 'tidak':
        print('Terimakasih Telah Menggunakan Layanan Kami')
        time.sleep(3)
        exit = True
        break



    


