# Tubes SISTER Siaga COVID-19
  
Cara menjalankan secara lokal:  
1. Ubah line 4 pada file `Client.py` yang sebelumnya `http://103.171.85.200:81` menjadi `http://localhost:[port yang diinginkan]`.
2. Pastikan file `database_nama.txt` dan `database_nik.txt` tersedia pada direktori aktif anda.
3. Jalankan server dengan argumen:
  ```sh
  $ python covidServer.py database_nik.txt database_nama.txt [port yang diinginkan]
  ```
4. Jalankan client dengan arguman:
  ```sh
  $ python Client.py
  ```