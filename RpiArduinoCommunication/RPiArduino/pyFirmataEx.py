import pyfirmata
import time
board = pyfirmata.Arduino('/dev/ttyUSB0')
led_pin = board.get_pin('d:11:o')
while True:
	led_pin.write(1)
	print("isik yaniyor")
	time.sleep(0.5)
	led_pin.write(0)
	print("isik sondu")
	time.sleep(0.5)
