import time
from w1thermsensor import W1ThermSensor
import httplib, urllib



while 1:
	sensor=W1ThermSensor()	
	#sicaklik okunuyor
	temp = sensor.get_temperature();
	#ThingSpeak field1:temp field'  key ile birlikte deger gonderiliyor
	params=urllib.urlencode({'field1':temp,'key':'P8IRV43361AO7ZZB'})
	headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
	#thingspeak ile 80 portundan baglanti kuruluyor
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST", "/update", params, headers)
        response = conn.getresponse()
        print("{} degeri yazdiriliyor").format(temp)
        print response.status, response.reason
        data = response.read()
        conn.close()
	time.sleep(0.5)
