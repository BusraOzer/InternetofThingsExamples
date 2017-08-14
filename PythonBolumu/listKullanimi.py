list1 = ['ayse', 'fatma','hayriye', 19, 20];

print list1
#listenin 2.indexindeki elemanin silinmesi
del list1[2];
print "Eleman silindikten sonra "
print list1

#bazi fonksiyonlar
list1.reverse()
print ("list1.reverse()",list1)
print("max(list1)",max(list1))
print("min(list1)",min(list1))
list1.sort()
print("list1.sort()",list1)

list1.append("tolga")
print("list1.append('tolga')",list1)

list1.insert(0,"busra")
print("list1.insert('busra')",list1)

list1.remove("tolga")
print("list1.remove('tolga')",list1)

print("list1.count('tolga')",list1.count('tolga'))

print("list1[1:4]",list1[1:4])
