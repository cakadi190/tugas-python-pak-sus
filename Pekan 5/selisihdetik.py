def convertWaktu(jam):
    jam = jam.split('.')
    h   = int(jam[0]) * 60 * 60
    m   = int(jam[1]) * 60
    s   = int(jam[2])

    return h + m + s

jam1 = input("Masukkan jam yang diinginkan (HH.mm.ss): ")
jam2 = input("Masukkan jam yang diinginkan (HH.mm.ss): ")
print("Jumlahnya adalah", convertWaktu(jam1) - convertWaktu(jam2), "detik")