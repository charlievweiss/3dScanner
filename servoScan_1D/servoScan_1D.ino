

#include <Servo.h>
Servo servoH;
Servo servoV; 
 
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
int sensorValue = 0; 
int posH = 70; // horizontal servo
int posV = 80; // vertical servo // we may want to change this, it might be too angled


void setup() {
  // put your setup code here, to run once:
  long baudRate = 9600;       // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     //
  servoH.attach(9); // initialize servos
  servoV.attach(10);
}

void loop() {
  delay(5000);
    while (posV <= 109) {
    // put your main code here, to run repeatedly:
    sensorValue = analogRead(analogInPin);
    delay(20);
    // sweep vertical up
    for (posV = 80; posV <= 110; posV += 1) {
      servoV.write(posV); 
      // sweep horizontal left
      if (posH < 100) {
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
      // sweep horizontal right
      else if (posH > 100) {
        for (posH = 110; posH >= 70; posH -=1) {
          servoH.write(posH); 
          delay(100);
          sensorValue = analogRead(analogInPin);
          Serial.print(posH); Serial.print(",");
          Serial.print(posV); Serial.print(",");
          Serial.println(sensorValue);
          delay(100);
        }
      }
      
      delay(20);
      }
    }

}
