'''Bu kod if/else ve loop konularinin pekistirmek
icin yazilmistir'''
import random
#0-100 arasi random bir sayi uretiliyor
sayi=random.randint(0,100)
tahmin=-1
tahminler=[-1]
#if ve while kullanimi
'''bu kodda bir mantik hatasi vardir.
Onu gormezden geliniz ev dongulere odaklaniniz.'''
while tahmin!= sayi:
	if(sayi>tahmin):
		print("Daha buyuk bir tahminde bulununuz!")
	else:
		print("Daha kucuk bir tahminde bulununuz!")
	tahmin=int(input("0-100 arasi bir tahmin giriniz:"))
	tahminler.append(tahmin)
print("Sayi dogru tahmin edildi.Denenen sayilar:")
#for kullanimi
for tahmin in tahminler:
	print(tahmin)
#baska bir yazim sekliyle
for i in range(len(tahminler)):
        print(tahminler[i])
print("Toplam Deneme Sayisi:{}").format(len(tahminler))
