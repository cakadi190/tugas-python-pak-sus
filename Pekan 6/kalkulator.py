def hitung(a, b, operasi):
	if(operasi == 1):
		hasil = a+b
	if(operasi == 2):
		hasil = a-b
	if(operasi == 3):
		hasil = a*b
	if(operasi == 4):
		hasil = a/b

	return hasil

print("Selamat datang di kalkulator.")
a = int(input("Masukkan angka pertama:"))
b = int(input("Masukkan angka kedua:"))
print("")
print("Pilih salah satu opsi dibawah:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
operasi = int(input("Masukkan opsi:"))
print("")

print("Hasilnya adalah:", hitung(a, b, operasi))