# This code takes a few inputs of voltage readings and their corresponding distances
# (obtained manually) and maps them to a polynomial. It then creates  graph of the
# result.

# It will take a few inputs of other positions and graph the error from the predicted
# distances on the same plot

import numpy as np
import matplotlib.pyplot as plt


class CalibrateSensor(object):
    def __init__(self):
        # Measured values for calibration
        self.x_calib = np.array([0, 50, 400, 650, 1023]) # x coordinates (voltage readings)
        self.y_calib = np.array([0, 20, 50, 100, 150]) # y coordinates (distances)
        # Measure values for error check
        self.x_check = np.array([20,300,500,800]) # voltage readings
        self.y_check = np.array([50,80,90,120]) # distances
        # x and y arrays for plotting
        self.x_calibPoly = []
        self.y_calibPoly = []
        self.x_checkPoly = []
        self.y_checkPoly = []
        self.y_error = []

    def createPolynomial(self, x, y):
        # takes array of x and y values and returns a calibrated set of y values for a polynomial
        # find coefficients for poly
        z = np.polyfit(x,y,3)
        # use coefficients to create poly
        polyFunc = np.poly1d(z)
        # create new array of x and y values
        new_x = np.linspace(0,1023,15)
        new_y = polyFunc(new_x)
        return new_x, new_y

    def run(self):
        # x and y array for calibration polynomial
        self.x_calibPoly, self.y_calibPoly = self.createPolynomial(self.x_calib, self.y_calib)
        # x and y array for check polynomial
        self.x_checkPoly, self.y_checkPoly = self.createPolynomial(self.x_check, self.y_check)
        # y varray for error
        self.y_error = np.subtract(self.y_calibPoly, self.y_checkPoly)

        # PLOT STUFF
        # calib polynomial
        plt.plot(self.x_calibPoly, self.y_calibPoly, 'ro', label='Original')
        # check polynomial
        plt.plot(self.x_checkPoly, self.y_checkPoly, 'bo', label='New')
        # error
        plt.plot(self.x_checkPoly, self.y_error, 'go', label='Error')
        plt.ylabel('Distance (cm)')
        plt.xlabel("Sensor Reading")
        plt.legend(loc='upper left')
        plt.title('Calibration Data')
        plt.show()
        # 
        plt.close('all') #ability to close figure

if __name__ == '__main__':
    func = CalibrateSensor()
    func.run()
