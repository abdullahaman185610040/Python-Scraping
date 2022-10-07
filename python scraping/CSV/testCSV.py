import csv

bukacsv = open('file.csv', 'r')
baca = csv.reader(bukacsv)

kode = []
namabarang = []
harga = []
jumlahbeli = []

i = 0
for row in baca :
    tanggal = row[0]
    pelanggan = row[1]
    if i != 0 :
        kode.append(row[2])
        namabarang.append(row[3])
        harga.append(row[4])
        jumlahbeli.append(row[5])
    i = i + 1
    
print("{:10} : {:15}".format("Tanggal", tanggal))
print("{:10} : {:15}".format("Pelanggan", pelanggan))
print("Item Barang")
print("{:10} : {:15} {:10} : {:10}".format("Kode", "Nama Barang", "Harga", "Jumlah"))
x = len(kode)

for i in range(x) :
    print("{:10} : {:15} {:10} : {:10}".format(kode[i], namabarang[i], harga[i], jumlahbeli[i]))

bukacsv.close()
    