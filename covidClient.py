# IF-43-02
# Siaga COVID-19

import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://103.171.85.200:81")

exit = False

while not exit:
    print("Pelaporan COVID-19")
    print("IF-43-02")
    
    # Input
    nik = "" # String
    nama_pelapor = "" # String
    nama_terduga = "" # String
    gejala = "" # String
    alamat = "" # String
    
    # Controller and Input
    while nik.replace(" ", "") == "":
        nik = input("Masukkan NIK Pelapor: ")
    while nama_pelapor.replace(" ", "") == "":
        nama_pelapor = input("Masukkan Nama Pelapor: ")
    while nama_terduga.replace(" ", "") == "":
        nama_terduga = input("Masukkan Nama Terduga: ")
    while gejala.replace(" ", "") == "":
        gejala= input("Masukkan Gejala Terduga: ")
    while alamat.replace(" ", "") == "":
        alamat= input("Masukkan Alamat Terduga: ")
        
    # Server request
    res = server.lapor(nik, nama_pelapor, nama_terduga, gejala, alamat)
    
    print(res)
    
    tmp_input = input("Apakah anda ingin melapor kembali? (y/N)")
    if tmp_input == "N":
        exit = True
    print("================================================")
