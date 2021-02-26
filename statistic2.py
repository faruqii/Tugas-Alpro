# list = [100,80,55,70,25,40,100,20,90,50]
import statistics
import numpy as np

list = []
n = int(input("masukan jumlah data :"))

for i in range(0, n):
    nilai = int(input())

    list.append(nilai)
    
list.sort()
average = statistics.mean(list)
median = statistics.median(list)
modus = statistics.mode(list)

print("Nilai Rata-Rata :",average)
print("Median :",median)
print("Modus :",modus)

print("Q1 :", np.quantile(list, .25 ))
print("Q2 :", np.quantile(list, .50))
print("Q3 :", np.quantile(list, .75)) 
