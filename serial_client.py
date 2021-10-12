from matplotlib import lines
import serial
import time
import matplotlib.pyplot as plt
import numpy as np

plot = False

serialPort = serial.Serial(port="COM7", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
serialString = ""  # Used to hold data coming over UART

if plot:
    dist = np.ones(360) * 5
    plt.ion()
    fig = plt.figure()
    ax  = fig.add_subplot(111, projection='polar')
    line1, = ax.plot(np.linspace(0, 2*np.pi, 360), dist)

f = open('testData.txt', 'a')

while 1:
    # Wait until there is data waiting in the serial buffer
    if serialPort.in_waiting > 0:
        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()
        # Print the contents of the serial data
        try:
            print(x:=serialString.decode("Ascii"), end='')
            if plot:
                x = serialString.decode('ascii')
                y = x.split()
                dist[int(y[1])] = y[3]
                line1.set_ydata(dist)
                fig.canvas.draw()
                fig.canvas.flush_events()

        except Exception as e:
            print(e)
            pass

