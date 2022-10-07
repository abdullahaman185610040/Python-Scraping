from xml.dom.minidom import parse

penjualan = parse("file.xml")

tanggal = penjualan.getElementsByTagName('tanggal')[0].firstChild.nodeValue
pelanggan = penjualan.getElementsByTagName('pelanggan')[0].firstChild.nodeValue
barang = penjualan.getElementsByTagName('barang')

print("{:10} : {:15}".format("Tanggal", tanggal))
print("{:10} : {:15}".format("Pelanggan", pelanggan))
print("Item Barang")
print("{:10} : {:15} {:10} : {:10}".format("Kode", "Nama Barang", "Harga", "Jumlah"))
jumlahItem = len(barang)

i = 0
while i < jumlahItem :
    kode = penjualan.getElementsByTagName('kode')[i].firstChild.nodeValue
    namabarang = penjualan.getElementsByTagName('namabarang')[i].firstChild.nodeValue
    harga = penjualan.getElementsByTagName('harga')[i].firstChild.nodeValue
    jumlahbeli = penjualan.getElementsByTagName('jumlahbeli')[i].firstChild.nodeValue
    print("{:10} : {:15} {:10} : {:10}".format(kode, namabarang, harga, jumlahbeli))
    i= i + 1