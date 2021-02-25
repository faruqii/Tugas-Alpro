'''
 {IS: Diberikan Data Wisata berupa:No Tiket,Nama Pengunjung,Jumlah Tiket}
 {FS:Cetak data No Tiket,Jumlah Tiket}

 Kamus = notiket : string
         pengunjung : string
         jumlahtiket : integer

Algoritma: 
output("Masukan No Tiket   :")
input(notiket)
output("Masukkan Nama Pengunjung  :")
input(pengunjung)
output("Jumlah Tiket :")
input(jumlahtiket)

output("No Tiket :"hasil input no tiket")

'''

notiket = str(input("Masukan No Tiket   :"))
pengunjung = str(input("Masukkan Nama Pengunjung  :"))
jumlahtiket = int(input("Jumlah Tiket :"))

print("No Tiket",notiket)
print("Jumlah Tiket",jumlahtiket)

print("Terima Kasih Sudah Membeli Tiket")
