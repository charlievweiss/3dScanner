

#include <Servo.h>
Servo servoH;
Servo servoV; 
 
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
int sensorValue = 0; 
int posH = 90; // horizontal servo
int posV = 120; // vertical servo // we may want to change this, it might be too angled


void setup() {
  // put your setup code here, to run once:
  long baudRate = 9600;       // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     //
  servoH.attach(9); // initialize servos
  servoV.attach(10);
}

void loop() {
    // put your main code here, to run repeatedly:
  servoV.write(posV);
  sensorValue = analogRead(analogInPin);
  delay(20);
  // sweep horizontal left
  while (posH < 110) {
    for (posH = 70; posH <= 110; posH +=1) {
      servoH.write(posH);
      delay(100);
      sensorValue = analogRead(analogInPin);
      Serial.print(posH); Serial.print(",");
      Serial.print(posV); Serial.print(",");
      Serial.println(sensorValue);
      delay(100);
    }
  }
}
