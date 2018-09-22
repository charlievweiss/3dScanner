# this takes readings from an arduino and maps them onto a graph to display
# an image of the object scanned

import serial
import numpy as np
import matplotlib.pyplot as plt
import time


class ScanObject(object):
    def __init__(self):
        self.arduinoComPort = "COM4"
        self.baudRate = 9600
        self.serialPort = serial.Serial(self.arduinoComPort, self.baudRate, timeout=1)
        self.rangeV = range(80,100)
        self.rangeH = range(70,110)
        self.readings = []
        self.x = []
        self.y = []
        self.z = []
        self.Zmat = np.zeros((len(self.rangeV), len(self.rangeH)))
        self.posH = 0 #temporay value for horizontal position of servo
        self.posV = 0 #temporay value for vertical position of servo
        self.reading = 0 # stores reading from IR sensor

    def getData(self):
        # ask for a line of data from the serial port, the ".decode()" converts the
        # data from an "array of bytes", to a string
        lineOfData = self.serialPort.readline().decode()
        # check if data was received
        if len(lineOfData.split(",")) > 2:
            # print(lineOfData)
            lineOfData = lineOfData.split(",")
            self.posH, self.posV, self.reading = lineOfData[0], lineOfData[1], lineOfData[2]
            print(str(self.posH) + ',' + str(self.posV) + ',' + str(self.reading))
            self.posH = int(self.posH)
            self.posV = int(self.posV)
            self.reading = int(self.reading)
            self.x.append(self.posH)
            self.y.append(self.posV)
            self.z.append(self.reading)
            self.Zmat[(self.posV-1-self.rangeV[0]), (self.posH-1-self.rangeH[0])] = self.reading
            # readings.append((posH, posV, IRsensor))
        else:
            time.sleep(.003)

    def plotDataContour(self, X, Y, Z):
        plt.contourf(X,Y,Z,20,cmap='RdGy')
        plt.colorbar()
        plt.xlabel('Horizontal position (degrees)')
        plt.ylabel('Vertical position (degress)')
        plt.title('Contour Map of Sensor Readings')
        plt.show()

    def run(self):
        while int(self.posV) <= 99:
            self.getData()
        print(len(self.z))
        # if len(self.z) == (len(self.rangeV) * len(self.rangeH)):
            # self.z = np.array(self.z)
            # self.z = z.reshape((len(self.rangeV), len(self.rangeH)))
        self.plotDataContour(self.rangeH,self.rangeV,self.Zmat)
        plt.close('all') #ability to close figure

if __name__ == '__main__':
    func = ScanObject()
    func.run()
