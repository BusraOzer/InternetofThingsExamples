#W1ThermSensor'un basit kullanimi bu ornekte gosterilmistir.
import time
from w1thermsensor import W1ThermSensor
while 1:
    #Butun sensorlerin sicakligi okunacak ise
    for sensor in W1ThermSensor.get_available_sensors():
         print("%s sensorunun olctugu sicaklik: %.2f"
         % (sensor.id, sensor.get_temperature()))
	
    #Sadece tipi DS18B20 olan sensorler'den sicaklik okunacak ise
    for sensor in W1ThermSensor.get_available_sensors([W1ThermSensor.THERM_SENSOR_DS18B20]):
         print("%s sensorunun olctugu sicaklik %.2f" 
	 % (sensor.id, sensor.get_temperature()))
