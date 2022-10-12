import math

def hitungPytaghoras(a, b):
    hasil = int(a)**2 + int(b)**2
    return math.sqrt(hasil)

a = int(input("Masukkan nilai sisi A: "))
b = int(input("Masukkan nilai sisi B: "))
result = hitungPytaghoras(a, b)

print("Sisi miringnya adalah:", result, "cm")