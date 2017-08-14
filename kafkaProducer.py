import time,datetime
from kafka import KafkaProducer
from hcsr04sensor import sensor
from w1thermsensor import W1ThermSensor

#hcsr04 sensoru icin 
trig_pin = 18
echo_pin = 24

#Buraya Kafka Serverin kurulu oldugu yerin ip adresini yaziyoruz
#Biz server'i bilgisayara kurdugumuz icin bilgisayarin ip adresini yazdik
producer = KafkaProducer(bootstrap_servers='10.42.0.1:9092')

#HC-SR04 Sensoru Icin
value = sensor.Measurement(trig_pin, echo_pin,
                           temperature=25,
                           unit='imperial',
                           round_to=2
                           )

while 1:
	#Sicaklik Olculmesi
	sensor=W1ThermSensor()
        temperature_in_celsius = sensor.get_temperature()
	t=datetime.datetime.now()
        print('Time:%s \t Sicaklik: %s Celcius') %(t,temperature_in_celsius)
	producer.send('RPiSensorData', b'Time:%s \t Olculen Sicaklik:%s Celcius'
	%(t,temperature_in_celsius))

	#Uzaklik Olculmesi
	raw_measurement = value.raw_distance(sample_size=10)
	metric_distance = value.distance_metric(raw_measurement)
	t=datetime.datetime.now()
    	print("Time:{} \t Olculen uzaklik: {} cm").format(t,metric_distance)
        producer.send('RPiSensorData', b'Time:%s \t Olculen Mesafe:%s cm ' 
	%(t,metric_distance))
        time.sleep(1)
