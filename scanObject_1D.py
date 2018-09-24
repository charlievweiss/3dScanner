# this takes readings from an arduino and maps them onto a graph to display
# an image of the object scanned

import serial
import numpy as np
import matplotlib.pyplot as plt
import time


class ScanObject(object):
    def __init__(self):
        self.arduinoComPort = "/dev/ttyACM0"#"COM4"
        self.baudRate = 9600
        self.serialPort = serial.Serial(self.arduinoComPort, self.baudRate, timeout=1)
        #self.rangeV = range(80,110)
        #self.rangeH = range(70,110)
        self.readings = []
        self.x = [] # horizontal angles
        self.y = [] # will be distances
        #self.Zmat = np.zeros((len(self.rangeV), len(self.rangeH)))
        self.posH = 0 #temporay value for horizontal position of servo
        self.reading = 0 # stores reading from IR sensor
        self.distance = 0 # will be distance calibrated from reading

    def getData(self):
        # ask for a line of data from the serial port, the ".decode()" converts the
        # data from an "array of bytes", to a string
        lineOfData = self.serialPort.readline().decode()
        # check if data was received
        if len(lineOfData.split(",")) > 2:
            # print(lineOfData)
            lineOfData = lineOfData.split(",")
            self.posH, self.posV, self.reading = lineOfData[0], lineOfData[1], lineOfData[2]
            #print(str(self.posH) + ',' + str(self.posV) + ',' + str(self.reading))
            self.posH = int(self.posH)
            self.reading = int(self.reading)
            self.distance = self.calibrateData(self.reading)
            # adjust with trig
            newX = self.distance * np.cos(np.radians(self.posH))
            newY = self.distance * np.sin(np.radians(self.posH))
            print("reading: " + str(self.reading) + " pos: " + str(self.posH))
            self.x.append(newX)
            self.y.append(newY)
            # readings.append((posH, posV, IRsensor))
        else:
            time.sleep(.003)

    def calibrateData(self, x):
        # stolen from calibrateSensorData code
        x_calib = np.array([464, 363, 265, 218, 203]) # voltage readings
        y_calib = np.array([24, 33, 45, 55, 60]) # distances
        coefficients = np.polyfit(x_calib,y_calib,3)
        polyFunc = np.poly1d(coefficients) # function from coefficients
        return polyFunc(x) # z values are now distances

    def plotData(self):
        plt.plot(self.x, self.y, 'bo')
        plt.xlabel('Horizontal position (cm)')
        plt.ylabel('Distance Away (cm)')
        plt.title('1D distance map of letter "H"')
        plt.show()

    def run(self):
        while int(self.posH) <= 109:
            self.getData()
        #print(len(self.z))
        # if len(self.z) == (len(self.rangeV) * len(self.rangeH)):
            # self.z = np.array(self.z)
            # self.z = z.reshape((len(self.rangeV), len(self.rangeH)))
        self.plotData()
        plt.close('all') #ability to close figure

if __name__ == '__main__':
    func = ScanObject()
    func.run()
