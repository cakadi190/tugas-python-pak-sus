import locale
import os

# Set bahasa dan pengaturan mata uang ke Rupiah dan Bahasa Indonesia
locale.setlocale(locale.LC_ALL, 'IND') 

# ----------------------------------- Space Print ---------------------------------- #
def printSpace(number):
	concat = ''
	for i in range(number):
		concat += " "
	
	return concat
# ----------------------------------- Space Print ---------------------------------- #

# ----------------------------------- Print Text ----------------------------------- #
def printText(json):
	for i in range(len(json)):
		name		= json[i]['name']
		price		= locale.currency(json[i]['price'])
		lName		= len(name)
		lPrice		= len(price)
		terminal	= os.get_terminal_size()
		sequence	= i + 1

		print(sequence, name, printSpace(terminal.columns - 6 - (lName + lPrice)), price)
# ----------------------------------- Print Text ----------------------------------- #

# ----------------------------------- Separator ----------------------------------- #
def printSeparator():
	terminal = os.get_terminal_size()
	print("+ ", end = '')
	for i in range(terminal.columns - 4):
		print("-", end = '')
	print(" +", end = '')
# ----------------------------------- Separator ----------------------------------- #

data = [
	{ "name":"Frutamin CocoBit Splash 350ml", "price":7000 },
	{ "name":"Minute Maid Juice Guava 300ml", "price":5100 }, 
	{ "name":"Indomaret Air Mineral 1500ml", "price":4700 },
	{ "name":"Aqua Mineral 600ml", "price":3200 },
	{ "name":"Minute Maid Juice Guava 300ml", "price":5100 }, 
	{ "name":"Aqua Mineral 1500ml", "price":5700 },
	{ "name":"Frutamin Coco Bit 350ml", "price":7000 }
]

print("")
print("Selamat datang di Mesin Minuman SukaMinum")
print("Pilih opsi dibawah")
printSeparator()
printText(data)
print("99 Membatalkan")
printSeparator()
opsi = int(input("Masukkan opsi:"))
print("")

def cekUang(nominal, harga):
	if(nominal < harga):
		print("Uang anda tidak cukup, coba lagi")
		nominal = int(input("Masukkan uang yang akan anda bayar:"))
		print("")

		cekUang(nominal, data[opsi - 1]['price'])
	else:
		print("Terima kasih, pembayaran kami terima.")

		if(nominal > data[opsi - 1]['price']):
			monChange = nominal - data[opsi - 1]['price']
			print("Kembalian anda adalah", locale.currency(monChange))

		print("Selamat berbelanja kembali.")

if(opsi == 99):
	print("Proses dibatalkan, goodbye!")
	quit()
else:
	nominal = int(input("Masukkan uang yang akan anda bayar:"))
	print("")
	cekUang(nominal, data[opsi - 1]['price'])