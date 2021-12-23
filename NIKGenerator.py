import time
import random
from datetime import timedelta, datetime

BASE = "321702" # Kode Daerah


with open('database_nik.txt', 'w') as file:
    waktu = datetime(1900, 1, 1)
    while waktu.year != 2022:
        tgl = waktu.day
        if tgl < 10:
            tgl = f"0{tgl}"
            
        bulan = waktu.month
        if bulan < 10:
            bulan = f"0{bulan}"
            
        tahun = waktu.year % 100
        if tahun < 10:
            tahun = f"0{tahun}"
        
        angkaRandomText = ""
        angkaRandom = random.randint(0,9999)
        if angkaRandom < 1000:
            angkaRandomText = f"0{angkaRandom}"
        if angkaRandom < 100:
            angkaRandomText = f"00{angkaRandom}"
        if angkaRandom < 10:
            angkaRandomText = f"000{angkaRandom}"
        
        if angkaRandomText == "":
            angkaRandomText = f"{angkaRandom}"
        
        nik = BASE + str(tgl) + str(bulan) + str(tahun) + angkaRandomText
        if len(nik) != 16:
            print("NIK tidak valid")
        
        file.write(f"{nik}\n")
        waktu += timedelta(days=1)
    