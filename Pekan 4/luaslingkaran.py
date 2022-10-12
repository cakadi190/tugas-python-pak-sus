# Definisi fungsi lingkaran
def luasLingkaran(ruji):
    phi     = float(22/7)
    hasil   = phi * ruji ** 2
    return hasil 

ruji  = int(input("Masukkan jari-jari lingkaran: "))    # Input jari-jari lingkaran
hasil = luasLingkaran(ruji)                             # Hasil penghitungan

print("Hasil penghitungannya adalah:", hasil)           # Menampilkan hasil