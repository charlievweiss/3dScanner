
import serial
arduinoComPort = "COM4"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)
readings = []
posH = 0 #temporay value so the for loop can be implemented
posV = 0 #temporay value so the for loop can be implemented
while int(posV) <= 110:
  #
  # ask for a line of data from the serial port, the ".decode()" converts the
  # data from an "array of bytes", to a string
  #
  lineOfData = serialPort.readline().decode()

  #
  # check if data was received
  #
  if len(lineOfData) > 0:
      posH, posV, IRsensor = lineOfData.split(",")
      print(posH + ',' + posV + ',' + IRsensor)
      posH = int(posH)
      posV = int(posV)
      IRsensor = int(IRsensor)
      readings.append((posH, posV, IRsensor))
