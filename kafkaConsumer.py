from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers='10.42.0.1:9092',
			 auto_offset_reset='earliest')

#print(consumer.topics()) #olusturulan topicleri gorebiliriz

consumer.subscribe(['RPiSensorData'])
for message in consumer:
	print(message)

