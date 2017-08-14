'''kullanimi
def myfunction():
statement1
statement2
'''
def toplama():
	print("Bu fonksiyon toplama islemi yapar") 
	a,b=input("sayi1,sayi2:")
	print("Toplam=",a+b)
def cikarma():
	print("Bu fonksiyon cikarma islemi yapar")
	a,b=(input("sayi1,sayi2:"))
	return a-b
def carpma(sayi1,sayi2):
	print(" Bu fonksiyon carpma yapar")
	print("Carpim=",sayi1*sayi2)

toplama()
sonuc=cikarma()
print("sonuc=cikarma()",sonuc)
carpma(5,sonuc)
