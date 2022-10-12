# Cek Tahun Kabisat
def cekKabisat(tahun):
    i      = 1
    result = 0

    while i <= int(tahun):
        if i % 4 == 0:
            result += 366
        else:
            result += 365
        i += 1
    return result

# Cek Bulan Kabisat
def cekBulanKabisat(tahun, bulan):
    result = 0
    i      = 1

    while i < int(bulan):
        if i == 2: # Cek kalau berada di bulan kedua lalu lakukan cek tahun kabisat
            if int(tahun) % 4 == 0:
                result += 29
            else:
                result += 28
        elif i % 2 == 1: # Cek kalau berada di bulan ganjil (Januari, Maret, ... Desember)
            result += 31
        else:
            result += 30
        i += 1
    return result

# Menghitung hari
def hitungHari(date):
    tanggal = date.split('-')
    tahun   = int(tanggal[0])

    # Cek Bulan yang otomatis set 12 ketika lebih dari 12 bulan
    if int(tanggal[1]) > 12:
        bulan = 12
    else:
        bulan = int(tanggal[1])

    # Cek Tanggal yang otomatis set maxDate sesuai dengan bulannya
    if tahun % 4 == 0:
        if bulan == 2:
            tanggal = 29
        elif bulan % 2 == 0:
            tanggal = 30
        else:
            tanggal = 31
    else:
        if bulan == 2:
            tanggal = 28
        elif bulan % 2 == 0:
            tanggal = 30
        else:
            tanggal = 31
    
    hasil = cekKabisat(tahun) + cekBulanKabisat(tahun, bulan) + tanggal
    return hasil

date1 = input("Masukkan tanggal yang diinginkan (format YYYY-MM-DD): ")
date2 = input("Masukkan tanggal yang diinginkan (format YYYY-MM-DD): ")
res   = hitungHari(date1) - hitungHari(date2)
print("Selisih hari pada tanggal yang anda masukkan adalah:", res, "hari")