# Menampilkan barang dan harga
def showGoods(data):
	for i in data:
		print(f"{i['name']} --------- {i['price']}")

# Menjalankan perintah
def main():
	print(f"Selamat datang di SiKasir!")
	print(f"Silahkan masukkan jumlah belanjaan anda.")
	total = int(input("Masukkan jumlah belanjaan anda:"))

	if(total >= 100000):
		data = [
			{ "name": "Minute Maid Pulpy Orange 600ml", "price": 8000 },
			{ "name": "Aqua Botol 600ml", "price": 3500 },
			{ "name": "Aqua Botol 1.5L", "price": 6000 },
		]

		print("Selamat, anda mendapatkan bonus belanja! Silahkan pilih salah satu produk dibawah.")
		showGoods(data)
		barang = int(input("Masukkan pilihan diatas:"))

		if(len(data[barang - 1]) > 0):
			print(f"Barang yang anda pilih adalah \"{data[barang - 1]['name']}\".")
			print("Terima kasih dan selamat berbelanja kembali!")
		else:
			main()
	else:
		print("Total belanjaan anda kurang dari 100.000IDR!")
		opsi = input("Apakah anda mengulanginya lagi? (Y/n):")

		if(opsi == "y" or opsi == "Y"):
			main()
		else:
			print("Terima kasih dan selamat jalan.")
			quit() # Mengakhiri terminal

# Menjalankan fungsi
main()