#      ******************************************************************
#      *                                                                *
#      *                                                                *
#      *    Example Python program that receives data from an Arduino   *
#      *                                                                *
#      *                                                                *
#      ******************************************************************


import serial

#
# NOTE: While this is running, you can not re-program the Arduino.  You must exit 
# this Phython program before downloading a sketch to the Arduino.
#


#
# Set the name of the serial port.  Determine the name as follows:
#	1) From Arduino's "Tools" menu, select "Port"
#	2) It will show you which Port is used to connect to the Arduino 
#
# For Windows computers, the name is formatted like: "COM6"
# For Apple computers, the name is formatted like: "/dev/tty.usbmodemfa141" 
#
arduinoComPort = "/dev/ttyACM0"


#
# Set the baud rate
# NOTE1: The baudRate for the sending and receiving programs must be the same!
# NOTE2: Set the baudRate to 115200 for faster communication
#
baudRate = 9600


#
# open the serial port
#
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)



#
# main loop to read data from the Arduino, then display it
#
while True:
  #
  # ask for a line of data from the serial port, the ".decode()" converts the 
  # data from an "array of bytes", to a string
  #
  lineOfData = serialPort.readline().decode()

  #
  # check if data was received
  #
  if len(lineOfData) > 0:
    #
    # data was received, convert it into 4 integers
    #
    a, b, c, d= (int(x) for x in lineOfData.split(','))

    #
    # print the results
    #
    print("a = " + str(a), end="")
    print(", b = " + str(b), end="")
    print(", c = " + str(c), end="")
    print(", d = " + str(d))


