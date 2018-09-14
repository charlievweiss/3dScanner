
const int analogInPin = A0;  // Analog input pin that the potentiometer is attached to
int sensorValue = 0; 

void setup() {
  // put your setup code here, to run once:
  long baudRate = 9600;       // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     //
}

void loop() {
  // put your main code here, to run repeatedly:
  sensorValue = analogRead(analogInPin);
  Serial.println(sensorValue);
  
  delay(50);

}
