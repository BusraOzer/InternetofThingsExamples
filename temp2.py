#W1ThermSensor'un basit kullanimi bu ornekte gosterilmistir.
import time
from w1thermsensor import W1ThermSensor
while 1:
	sensor=W1ThermSensor()
	temperature_in_celsius = sensor.get_temperature()
	temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
	temperature_in_kelvin=sensor.get_temperature(W1ThermSensor.KELVIN)
	temperature_in_all_units = sensor.get_temperatures([
    	W1ThermSensor.DEGREES_C,
    	W1ThermSensor.DEGREES_F,
    	W1ThermSensor.KELVIN])
	
	#Sicakliklarin Yazdirilmasi
	print('Celcius: %s') %temperature_in_celsius
	print('Fahrenheit: %s') % temperature_in_fahrenheit
	print('Kelvin: %s') %temperature_in_kelvin
	
	print('Celcius-Fahrenheit-Kelvin: %s') %temperature_in_all_units
	time.sleep(1)
