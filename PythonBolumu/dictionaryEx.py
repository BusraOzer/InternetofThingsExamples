#dictionary kullanimi
dict = {'name': 'tolga', 'age': '25', 'name':'busra','age':'24'}
print ("dict['name']: ", dict['name'])
#type of variables
print("type(dict):",type(dict))
#kopyala
dict1=dict.copy()
#python dictionary tekrarlanmis keyleri desteklememektedir.
print("dict1.items()",dict1.items())

print("dict1.keys()",dict1.keys(),"\n dict1.values()",dict1.values())

dict1.update({'soyad':'ozer'})
print("dict1.keys()",dict1.keys(),"\n dict1.values()",dict1.values())

for value in dict1.values():
	print("value:",value)

#butun elementleri sil
dict.clear()
print("dict.keys()",dict.keys(),"\n dict.values()",dict.values())

