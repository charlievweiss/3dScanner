# This code takes a few inputs of voltage readings and their corresponding distances
# (obtained manually) and maps them to a polynomial. It then creates  graph of the
# result.

# It will take a few inputs of other positions and graph the error from the predicted
# distances on the same plot

import numpy as np
import matplotlib.pyplot as plt

# Calibration points
# voltage readings

# Measured values for calibration
x_calib = np.array([0, 50, 400, 650, 1023]) # x coordinates (voltage readings)
y_calib = np.array([0, 20, 50, 100, 150]) # y coordinates (distances)
z_calib = np.polyfit(x_calib,y_calib,3) # gives coefficients of polynomial

# Measure values for error check
x_check = np.array([20,300,500,800]) # voltage readings
y_check = np.array([50,80,90,120]) # distances
z_check = np.polyfit(x_check,y_check,3)

# Polynomial function for calibration
calibPolyFunc = np.poly1d(z_calib) 

# calculate x's and y's for calibration polynomial
x_calibPoly = np.linspace(0, 1023, 15)
y_calibPoly = calibPolyFunc(x_calibPoly)

###
###

# Polynomial function for check
checkPolyFunc = np.poly1d(z_check)

# calculate x's and y's for check polynomial
x_checkPoly = np.linspace(0,1023,15)
y_checkPoly = checkPolyFunc(x_checkPoly)

###
###

# Compare two polynomials
y_error = np.subtract(y_calibPoly,y_checkPoly)
print(y_error)

# PLOTS 

# calib polynomial
plt.plot(x_calibPoly, y_calibPoly, 'ro')
plt.ylabel('some numbers')
plt.show()

# 

plt.close('all') #ability to close figure