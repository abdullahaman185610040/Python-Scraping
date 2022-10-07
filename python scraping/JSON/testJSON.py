import json

bukajson = open('file.json', 'r')

data = json.load(bukajson)

print("{:10} : {:15}".format("Tanggal", data['tanggal']))
print("{:10} : {:15}".format("Pelanggan", data['pelanggan']))
print("Item Barang")
print("{:10} : {:15} {:10} : {:10}".format("Kode", "Nama Barang", "Harga", "Jumlah"))

for barang in data['barang'] :
    print("{:10} : {:15} {:<10} : {:<10}".format(barang['kode'], barang['namabarang'], barang['harga'], barang['jumlahbeli']))