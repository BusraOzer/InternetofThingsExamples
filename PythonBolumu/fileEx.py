import os

print(os.getcwd()) #pwd komutunun isini yapar
if not os.path.exists(os.getcwd()+"/asalSayilar"):
	os.mkdir('asalSayilar') #yeni bir klasor olusturur
os.chdir('asalSayilar') # cd klasor komutunun isini yapar
print(os.getcwd()) #pwd
file=open(os.getcwd()+"/asallar.txt","a+") 
'''acilan dosya hem okuma yapmak hem de yazmak icin kullanilacaltir.
Dosya her defasinda yeniden olusturulmayacak,icindeki veriler 
apend edilecektir. Bunun isin a+ parametresini kullandik.'''

#Dosya Okuma
sayilar=file.read()
print(sayilar+"Okundu")

for p in range(2, 1000+1):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print p,
	file.write(str(p)+"\t")
print 'Done'
file.close()

