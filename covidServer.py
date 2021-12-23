# IF-43-02
# Siaga COVID-19
# Args: file.py database_nik.txt database_nama.txt PORT
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import sys
from datetime import timedelta, datetime
import random

PORT = int(sys.argv[3])

def readlines(path):
    files = open(path, "r", encoding="utf-8", errors="replace")
    file_contents = files.read()
    lines = file_contents.splitlines()
    files.close()
    return lines

# Read NIK from Databases
nik_list = readlines(sys.argv[1])
# Read Petugas from Databases
nama_list = readlines(sys.argv[2])
# Setup RPC Server
class RequestHandler(SimpleXMLRPCRequestHandler):
  rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(("localhost", PORT), RequestHandler) as server:
    
    def lapor(nik: str, nama_pelapor:str, nama_terduga:str, gejala:str, alamat:str):        
        # Check valid nik
        if nik not in nik_list:
            return "Server: NIK tidak valid"
        
        # Setup return penjemputan 1 hari setelah pelaporan
        waktu = datetime.now()
        waktu += timedelta(days=1)
        
        # Setup return jumlah orang yang berangkat
        jumlah = random.randint(5,10)
        
        # Setup nama orang yang berangkat
        list_org = []
        for i in range(jumlah):
            ulang = True
            while ulang:
                orang = nama_list[random.randint(0,len(nama_list))]
                if orang not in list_org:
                    list_org.append(orang)
                    ulang = False
            
        return f'Server: Akan dilakukan penjemputan pada {waktu.strftime("%m/%d/%Y, %H:%M:%S")} WIB dengan jumlah penjemput {jumlah} dengan petugas bernama {", ".join(list_org)}'
        
        
    server.register_function(lapor, 'lapor')
    
    print("Server listening on port", PORT)
    server.serve_forever()
        