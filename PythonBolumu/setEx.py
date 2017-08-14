from sets import Set
#A-B-C kumeleri
A=Set(['tolga','busra','ahmet','salih','levent'])
B=Set(['tulay','bayram','cabir','tolga'])
C=Set(['tolga','gunay','guven','gursel','zafer','levent'])

#3 kumenin birlesimi
union= A | B | C #union
print("union:",union)
#2 kumenin kesisimi
intersection= A & B #intersection
print("intersection:",intersection)
#iki kumenin farki
difference= A-B
print("difference:",difference)

for group in [A,B,C]: 
	group.discard('bayram')         #silme 
	print group
