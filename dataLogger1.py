import time,datetime
from w1thermsensor import W1ThermSensor
import sys

startHour=-1
while 1:
	date=datetime.datetime.now()
	newHour=date.hour
	if startHour!=newHour:
		startHour=date.hour
		#her saat icin ayri bir log dosyasi adi
		#saat 12 icin log adi 20160926-120000.log olacak
		filename = time.strftime("%Y%m%d-%H0000")+".log"
		#dosyayi ac, eger dosya yok ise olustur
		datafile = open(filename, 'a')
	#Butun sensorlerin sicakligi okunacak ise
    	for sensor in W1ThermSensor.get_available_sensors():
		#ekrana yaz
        	print("%s sensorunun olctugu sicaklik: %.2f"
         	% (sensor.id, sensor.get_temperature()))
		#dosyaya yaz
		datafile.write("%s \t %s \t %f \n"
                % (date,sensor.id, sensor.get_temperature()))
		time.sleep(2)
