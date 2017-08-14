import math
from fractions import Fraction
var1=input("var1 icin deger giriniz:")
var2=input("var2 icin deger giriniz:")
#4 islem
result=var1+var2
print("sonuc=",result)
result=var1-var2
print("sonuc=",result)
result=var1*var2
print("sonuc=",result)
result=var1/var2
print("sonuc=",result)

#bazi fonksiyonlar
#faktoriyel
result=math.factorial(int(var1+var2))
print("sonuc=",result)
#uslusayilar
result=math.pow(var1,var2);
print("sonuc=",result)
