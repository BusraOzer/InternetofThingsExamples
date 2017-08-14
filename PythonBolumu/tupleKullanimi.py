# -*- coding: utf-8 -*- 
#degiskenler
t1=(1,2,3,4,'tolga','5',12.4)
t2=('ayse','fatma','hayriye',15)
#tuple'in 3.elemani yazidirldi
print("t1[3]",t1[3])
#tuple'in ilk 4 elemani yazdirildi
print("t2[0:4]",t2[0:4])

#tuplelarin birlestirilmesi
t3=t1+t2
print("t3",t3)

'''tuple'in silinmesi
del t3
print("t3",t3)
print("t2[0:4]",t2[0:4])
'''

#Bazi Fonksiyonlar
print("len(t2)",len(t2))
print("max(t1)={} max(t2)={}").format(max(t1),max(t2))
print("min(t1)={} min(t2)={}").format(min(t1),min(t2))
