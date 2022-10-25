# Operasi hitung
# 
# @param a int Angka pertama
# @param b int Angka kedua
# @param opsi int Operator yang diinginkan
def operator(a, b, opsi):
    if(opsi == 1):
        print(f"Hasil penjumlahan dari {a}+{b} adalah {a+b}")
    elif(opsi == 2):
        print(f"Hasil pengurangan dari {a}-{b} adalah {a-b}")
    elif(opsi == 3):
        print(f"Hasil kali dari {a}*{b} adalah {a*b}")
    elif(opsi == 4):
        print(f"Hasil kali dari {a}/{b} adalah {a/b}")
    else:
        print("Maaf, pilihan anda salah!")
    
def main():
    a = int(input("Masukkan nilai pertama:"))
    b = int(input("Masukkan nilai kedua:"))

    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("99. Keluar")
    opsi = int(input("Masukkan opsi penghitungan:"))

    if(opsi == 99):
        quit()
    elif(opsi != 99):
        operator(a, b, opsi)

        opsi = input("Apakah anda akan mengulanginya lagi? (Y/n):")
        if(opsi == 'Y' or opsi == 'y'):
            main()
        else:
            quit() # Keluarkan dari terminal
    else:
        main()

print("Kalkulator simpel")
main()