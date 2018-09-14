
import serial
arduinoComPort = "COM4"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
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
      print(lineOfData)
