def bol():
	try:
		sayi1=int(input("Bolunecek sayiyi giriniz:"))
		sayi2=int(input("Bolen sayiyi giriniz:"))
	except ValueError as e:
		print("Hata: Sayi girmeniz gerekmektedir!:",e)
	except KeyboardInterrupt as e:
		print("Hata:Script kapatiliyor",e)
	try:
		bolum=sayi1/sayi2
		print("Sonuc=",bolum)
	except ZeroDivisionError as e:
		print("Hata:Bolen sayi 0 olomaz!:",e)

bol()
