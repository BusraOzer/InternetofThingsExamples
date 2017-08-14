#include <Wire.h>

#define SLAVE_ADDRESS 0x04
int number = 0;
int state = 0;


// recieveData fonksiyonu
void receiveData(int byteCount){

while(Wire.available()) {
number = Wire.read();
Serial.print("data alindi: ");
Serial.println(number);

if (number%2 == 1){

if (state == 0){
digitalWrite(13, 1); // ledi yak
state = 1;
}
else{
digitalWrite(13, 0); //ledi sondur
state = 0;
}
}
}
}

// sendData fonksiyonu
void sendData(){
Wire.write(number);
}

void setup() {
pinMode(13, OUTPUT);
Serial.begin(9600);
//i2c'yi slave olarak baslat
Wire.begin(SLAVE_ADDRESS);

// i2c iletisimi
Wire.onReceive(receiveData);
Wire.onRequest(sendData);

Serial.println("Hazir!");
}

void loop() {
delay(100);
}

