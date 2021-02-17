# 1. Buatlah program entry sejumlah array (tergantung input user) dan cari nilai rata-rata dari nilai array yang diinputkan tersebut.
# 2. Buat program entry sejumlah array (tergantung input user) dan cari nilai maksimum serta minimum dari nilai array yang diinputkan tersebut.

list = []

n = int(input("masukan jumlah data :"))

for i in range(0, n):
    element = int(input())

    list.append(element)

list.sort()

sum = sum(list)
length = len(list)

minimum = min(list)
maximum = max(list)
average = sum/length

print("Array", list)
print("Nilai Minimum", minimum)
print("Nilai Maximum", maximum)
print("Rata-Rata", average)
