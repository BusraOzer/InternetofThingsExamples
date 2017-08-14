import re

file=open("regexTest","r+")
for f in file:
	searchObj = re.search(r"[\w\.-]+@[\w\.-]+", f)
	if(searchObj):
		print("Bulunan mail adresi:",searchObj.group(0))
