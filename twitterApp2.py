#!/usr/bin/python
import Adafruit_DHT
import sys
import datetime,time
from twython import Twython

CONSUMER_KEY = '***********************************************'
CONSUMER_SECRET = '********************************************'
ACCESS_KEY = '*************************************************'
ACCESS_SECRET = '**********************************************'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

# Bizim kullandigimiz sensor DHT11
sensor = Adafruit_DHT.DHT11

#Biz data bacagini GPIO25'e bagladigimizdan 
pin = 25
dateTime=datetime.datetime.now()

#Sensorden daha dogru sonuc almak icin 15 defa veri okur ve ortalamasini yazar
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
	mesaj='#kars Datetime={0}  Sicaklik={1:0.4f} Santigrad  Nem={2:0.4f}%'.format(dateTime,temperature, humidity)
	print('Date={0} Sicaklik={1:0.4f} Santigrad  Nem={2:0.4f}%'.format(dateTime,temperature, humidity))
else:
   	mesaj='Okurken bir hata meydana geldi'
    	print('Okurken bir hata meydana geldi')

api.update_status(status=mesaj)
