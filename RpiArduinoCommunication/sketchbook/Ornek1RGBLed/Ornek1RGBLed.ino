int redPin = 11;
int greenPin = 10;
int bluePin = 9;
 
//uncomment this line if using a Common Anode LED
//#define COMMON_ANODE

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
  for(int i=0;i<256;i++)
  {
    for(int j=0;j<256;j++)
    {
       for(int k=0;k<256;k++)
       {
         setColor(i,j,k);
         Serial.print(i);
         Serial.print(" ");
         Serial.print(j);
         Serial.print(" ");
         Serial.println(k);
         delay(0.1);
       }
    }
  }
}
