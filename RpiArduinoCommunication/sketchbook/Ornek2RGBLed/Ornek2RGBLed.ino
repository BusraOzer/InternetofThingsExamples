int redPin = 11;
int greenPin = 10;
int bluePin = 9;
 
void setColor(int red, int green, int blue)
{
  #ifdef COMMON_ANODE
    red = 255 - red;
    green = 255 - green;
    blue = 255 - blue;
  #endif
  analogWrite(redPin, red);
  analogWrite(greenPin, green);
  analogWrite(bluePin, blue);
}
 
void setup()
{
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);  
  Serial.begin(9600);
}
 
void loop()
{
 if(Serial.available())
 {
   setColor(Serial.read(),Serial.read()%100,Serial.read()%17);
 }
 delay(500);
}
