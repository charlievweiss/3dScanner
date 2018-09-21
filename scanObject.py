# this takes readings from an arduino and maps them onto a graph to display
# an image of the object scanned

import serial
import numpy as np
import matplotlib.pyplot as plt


class ScanObject(object):
    def __init__(self):
        self.arduinoComPort = "COM4"
        self.baudRate = 9600
        self.serialPort = serial.Serial(self.arduinoComPort, self.baudRate, timeout=1)
        self.readings = []
        self.x = []
        self.y = []
        self.z = []
        self.posH = 0 #temporay value for horizontal position of servo
        self.posV = 0 #temporay value for vertical position of servo
        self.reading = 0 # stores reading from IR sensor

    def getData(self):
        # ask for a line of data from the serial port, the ".decode()" converts the
        # data from an "array of bytes", to a string
        lineOfData = serialPort.readline().decode()
        # check if data was received
        if len(lineOfData) > 0:
            self.posH, self.posV, self.reading = lineOfData.split(",")
            print(self.posH + ',' + self.posV + ',' + self.reading)
            self.posH = int(self.posH)
            self.posV = int(self.posV)
            self.reading = int(self.reading)
            self.x.append(self.posH)
            self.y.append(self.posV)
            self.z.append(self.reading)
            #readings.append((posH, posV, IRsensor))

    def plotDataContour(self, X, Y, Z):
        plt.contourf(X,Y,Z,20,cmap='RdGy')
        plt.colorbar()
        plt.xlabel('Horizontal position (degrees)')
        plt.ylabel('Vertical position (degress)')
        plt.title('Contour Map of Sensor Readings')
        plt.show()

    def run(self):
        while int(posV) <= 110:
            self.getData()
        self.plotDataContour()
        plt.close('all') #ability to close figure

if __name__ == '__main__':
    func = ScanObject()
    func.run()
