import numpy

x = np.array([0, 20, 50, 100, 150]) #x coordinates (distances)
y = np.array([0, 136.4, 341, 682, 1023]) #y coordinates (voltage readings)
z = np.polyfit(x,y,3) #