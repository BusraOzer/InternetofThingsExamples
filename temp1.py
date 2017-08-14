#Sicaklik Okuma Ornegi 2
import time
import datetime

while 1:
	#w1_slave dosyasini ac 
	tFile=open("/sys/bus/w1/devices/28-0000074ed11b/w1_slave")
	#w1_slave dosyasinin tamamini oku
	text=tFile.read()
	#dosyayi kapat
	tFile.close()
	#text'in 2.satir 10. sutununu al
	tData=text.split("\n")[1].split(" ")[9]
	'''Eger okunan sicaklik degeri 1000'e bolunurse
 santigrad cinsinden degeri bulunur.'''
	tData=float(tData[2:])/1000
	#Simdiki zaman
	i=datetime.datetime.now()
	#ekrana 2.satir 10.sutunu yaz
	print '%s  %f Santigrad' %(i,tData)
	time.sleep(1)
