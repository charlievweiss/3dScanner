

#include <Servo.h>
Servo servoH;
Servo servoV; 
 
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
int sensorValue = 0; 
int posH = 60; // horizontal servo
int posV = 70; // vertical servo // we may want to change this, it might be too angled


void setup() {
  // put your setup code here, to run once:
  long baudRate = 9600;       // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     //
  servoH.attach(9); // initialize servos
  servoV.attach(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorValue = analogRead(analogInPin);
  Serial.println(sensorValue);
  delay(50);
  // sweep vertical up
  for (posV = 70; posV <= 110; posV += 1) {
    // sweep horizontal left
    for (posH = 60; posH <= 120; posH +=1) {
      servoH.write(posH);
      delay(20);
    }
    // sweep horizontal right
    for (posH = 120; posH >= 60; posH -=1) {
      servoH.write(posH); 
      delay(20);
    }
    servoV.write(posV); 
    delay(50)
    }
  

}
