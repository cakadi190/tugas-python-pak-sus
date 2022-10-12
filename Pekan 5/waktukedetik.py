def convertWaktu(jam):
    jam = jam.split(':')
    h   = int(jam[0]) * 60 * 60
    m   = int(jam[1]) * 60
    s   = int(jam[2])

    return h + m + s

jam = input("Masukkan jam yang diinginkan (HH:mm:ss): ")
print("Jumlahnya adalah", convertWaktu(jam), "detik")