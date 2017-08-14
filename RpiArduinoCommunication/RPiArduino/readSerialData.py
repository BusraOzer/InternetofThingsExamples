import serial
#Arduino'nun dosya yolu ve 9600 bps
#Eger bu dosya yolunu ogrenmek istiyorsaniz ls /dev/tty* i kullanabilirsiniz
ser=serial.Serial('/dev/ttyUSB0',9600)
while 1:
	print(ser.readline())
