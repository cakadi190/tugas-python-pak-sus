# Definisikan Fungsi
def CekDuaBilangan(a, b):
    pertama = a
    kedua   = b

    if(a > b):
        print("Nilai", a, "lebih besar daripada", b)
    elif(a < b):
        print("Nilai", b, "lebih besar daripada", a)
    else:
        print("Kedua bilangan sama")


a = int(input("Masukkan nilai pertama: "))
b = int(input("Masukkan nilai kedua: "))

CekDuaBilangan(a,b)