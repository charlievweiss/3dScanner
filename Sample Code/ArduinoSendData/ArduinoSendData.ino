
//      ******************************************************************
//      *                                                                *
//      *                                                                *
//      *     Example Arduino program that transmits data to a laptop    *
//      *                                                                *
//      *                                                                *
//      ******************************************************************


//
// setup function to initialize hardware and software
//

//constants
int sensorPin = 0; // Analog pin for IR sensor

//variables
int sensorValue = 0; //reading from IR
int sensorMin = 1023; // minimum sensor value
int sensorMax = 0; //maximum sensor value

void setup()
{ 
  //
  // start the serial port
  //
  long baudRate = 9600;       // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     // NOTE2: Set the baudRate to 115200 for faster communication
  //Serial.println("BEGIN");

  //calibrate during first five seconds
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
  Serial.println("END");
}



//
// main loop
//
void loop() 
{  
  int a, b, c, d;

  a = 0;
  b = 0;
  c = 0;
  d = 0;

  //
  // loop: calculate the data, then send it from the Arduino to the phython program
  //
  while(true) {
    //
    // here is where you update the data to be sent
    //
    a = a + 1;    // a counts by 1s
    b = b + 2;    // b counts by 2s
    c = c + 3;    // c counts by 3s
    d = d + 4;    // d counts by 4s
    
    
    //
    // transmit one line of text to phython with 4 numeric values
    // NOTE: commas are sent between values, after the last value a Newline is sent
    //
    Serial.print(a);    Serial.print(",");
    Serial.print(b);    Serial.print(",");
    Serial.print(c);    Serial.print(",");
    Serial.println(d);  Serial.print(",");
    

    //
    // delay after sending data so the serial connection is not over run
    //
    delay(400);
  }
}
