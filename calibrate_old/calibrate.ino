// Calibrate distance sensor
// get set of readings for known distances and determine mathematical relationship between
//physical distance and sensor voltage reading

//constants
int sensorPin = 0; // Analog pin for IR sensor

//variables
int sensorValue = 0; //reading from IR
int sensorMin = 1023; // minimum sensor value
int sensorMax = 0; //maximum sensor value


void setup() {
  Serial.begin(9600);

  /*//calibrate during first 10 seconds
    while (millis() < 10000) {
    sensorValue = analogRead(sensorPin);

    // record the maximum sensor value
    if (sensorValue > sensorMax) {
      sensorMax = sensorValue;
    }

    // record the minimum sensor value
    if (sensorValue < sensorMin) {
      sensorMin = sensorValue;
    }
  }
  Serial.println(sensorMax);
  Serial.println(sensorMin);*/
}

void loop() {
  // read the sensor:
  sensorValue = analogRead(sensorPin);

  // apply the calibration to the sensor reading
  sensorValue = map(sensorValue, sensorMax, sensorMin, 20, 60);

  // in case the sensor value is outside the range seen during calibration
  sensorValue = constrain(sensorValue, 20, 60);
  //Serial.println(sensorMax);
  //Serial.println(sensorMin);
}
