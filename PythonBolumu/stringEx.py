str="""Bizim akil, mantik, zeka ile hareket etmek en belirgin ozelligimizdir. 
Butun hayatimizi dolduran olaylar bu gercegin delilidirler."""
print(str)

#string'i parcalamak
list=str.split()
print("str.split()",list)
#noktaya gore parcalamak
list=str.split(".")
print("str.split('.')",list)

str1='Mustafa Kemal Ataturk'
#string birlestirme
str=str+str1
print("str=str+str1",str)

#isdigit()
yas=input('yasinizi giriniz:')
if (yas.isdigit()):
	print("Yasiniz:",yas)
else:
	print("Dogru giris yapmadiniz!")


#find
print("find:","mantik" in str)
print("find:",str.find("akil"))
