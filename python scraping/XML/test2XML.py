import xml.etree.ElementTree as ET

tree = ET.parse('file.xml')
root = tree.getroot()

tanggal = root.find('tanggal').text
pelanggan= root.find('pelanggan').text

print("{:10} : {:15}".format("Tanggal", tanggal))
print("{:10} : {:15}".format("Pelanggan", pelanggan))
print("Item Barang")
print("{:10} : {:15} {:10} : {:10}".format("Kode", "Nama Barang", "Harga", "Jumlah"))

for barang in root.findall('barang') :
    kode = barang.find('kode').text
    namabarang = barang.find('namabarang').text
    harga = barang.find('harga').text
    jumlahbeli = barang.find('jumlahbeli').text
    print("{:10} : {:15} {:10} : {:10}".format(kode, namabarang, harga, jumlahbeli))