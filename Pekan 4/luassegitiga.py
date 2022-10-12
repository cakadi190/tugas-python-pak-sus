# Deklarasi fungsi
def luasSegitiga(a, t):
	luas = a * t * 0.5
	return luas

alas   = int(input("Masukkan nilai panjang alas:"))		# Input alas
tinggi = int(input("Masukkan nilai panjang tinggi:"))	# Input tinggi
hasil  = luasSegitiga(alas, tinggi)						# Hitung hasil

print("Hasil penghitungannya adalah:", hasil) # Output