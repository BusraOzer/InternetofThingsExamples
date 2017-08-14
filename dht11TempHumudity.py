#!/usr/bin/python

import Adafruit_DHT

# Bizim kullandigimiz sensor DHT11
sensor = Adafruit_DHT.DHT11

#Biz data bacagini GPIO25'e bagladigimizdan 
pin = 25

#Sensorden daha dogru sonuc almak icin 15 defa veri okur ve ortalamasini yazar
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Sicaklik={0:0.1f} Santigrad  Nem={1:0.1f}%'.format(temperature, humidity))
else:
    print('Okurken bir hata meydana geldi')
