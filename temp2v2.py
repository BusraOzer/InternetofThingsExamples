#W1ThermSensor'un basit kullanimi bu ornekte gosterilmistir.
import time
from w1thermsensor import W1ThermSensor
while 1:
  sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0000074ed11b")
  temperature_in_celsius = sensor.get_temperature()
	
  #Birden fazla sensor var ise ve specific bir sensorden okuma yapmak istiyor isek
  print('28-0000074ed11b sensorunun olctugu sicaklik(C): %s') %temperature_in_celsius
	
