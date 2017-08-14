#!/usr/bin/python
import re

mail = "tolgabuyuktanir@.com";

#regular expression
searchObj = re.search( r'(.*)@(.*\.)(.*)', mail)

if searchObj:
	print "searchObj.group() : ", searchObj.group()
   	print "searchObj.group(1) : ", searchObj.group(1)
   	print "searchObj.group(2) : ", searchObj.group(2)
   	print "searchObj.group(3) : ", searchObj.group(3)
else:
   print "Nothing found!!"

#mailin valid olup olmadigi
#eger mail adresi formata uygun ise yazar degilse bos gosterir
searchObj=re.findall(r"\w+@\w+\.(?:com|in)",mail)
print "mail : ", searchObj

deneme="tolga Buyuktanir.lkngolnobg norgbourtnhgou rtguo hrtuort.uhg.ruhtgu.rthgu hyuhrtyuhgyygygygryegfygrfgy?rggefr"
d=re.search(r'(Bi*)',deneme)
print d.group()
