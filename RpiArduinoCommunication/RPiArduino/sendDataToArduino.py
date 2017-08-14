import serial
import struct
ser=serial.Serial("/dev/ttyUSB0",9600);
while 1:
	for i in range(0,226):
		'''ASCII karakterler gonderildiginde kod hata verecektir.
		Dolayisiyle raw data gonderilmesi gerekmektedir'''
		ser.write(struct.pack('I',i))


