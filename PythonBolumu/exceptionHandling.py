while 1:
	try:
		input=int(input("Bir sayi giriniz:"))
		break
	except ValueError as e:
		print("Hatali giris yaptiniz.Lutfen tekrar deneyin:",e)
