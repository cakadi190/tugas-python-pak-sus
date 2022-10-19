import os
import locale

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

# ----------------------------------- Runner ----------------------------------- #
def cekBonus(total, repeat = False):
	if(int(total) > 100000):
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

		if(repeat == False): 
			print("Selamat, anda mendapatkan bonus! Silahkan pilih beberapa opsi bonus yang tersedia dibawah.")
			printSeparator()
			printText(data)
			printSeparator()
		else:
			print("Maaf, pilihan anda salah. Mohon ulangi lagi pilihan sesuai dengan pilihan diatas ya?")

		opsi = int(input("Masukkan opsi diatas:"))

		if(opsi > len(data)):
			cekBonus(total, True)
		else:
			print("")
			print("Anda memilih bonus dibawah ini:")
			print(data[opsi - 1]['name'], "seharga", locale.currency(data[opsi - 1]['price']))
			print("")
			print("Terima kasih, dan selamat berbelanja kembali.")
	else:
		print("")
		print("Maaf ya, anda belum beruntung. Karena total belanja anda kurang dari Rp100.000,00")
# ----------------------------------- Runner ----------------------------------- #

print("Selamat datang di SIKASIR, silahkan masukkan jumlah harga belanja anda")
total = int(input("Masukkan jumlah belanjaan anda:"))
cekBonus(total)