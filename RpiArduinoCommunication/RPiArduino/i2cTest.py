import smbus
import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# Arduino kodunda kullandigimiz adress
address = 0x04

def writeNumber(value):
	bus.write_byte(address, value)
	# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
	# number = bus.read_byte_data(address, 1)
	return number

while True:
	var = input("Sayi gir(1-9): ")
	if not var:
		continue

	writeNumber(var)
	print("RPI: Merhaba Arduino, Gonderdigin mesaj: ", var)
	time.sleep(1)

	number = readNumber()
	print("Arduino: Merhaba RPI, Aldigim mesaj:\n ", number)
