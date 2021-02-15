list = []

n = int(input("masukan jumlah data :"))

for i in range(0, n):
    element = int(input())

    list.append(element)

sum = sum(list)
length = len(list)

minimum = min(list)
maximum = max(list)
average = sum/length

print("Array", list)
print("Nilai Minimum", minimum)
print("Nilai Maximum", maximum)
print("Rata-Rata", average)
