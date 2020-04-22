import numpy as np
import matplotlib.pyplot as plt
import serial
import collections


# https://www.thepoorengineer.com/en/arduino-python-plot/

class serialPlot:
    def __init__(self, serialPort ='/dev/ttyACM0', serialBaud = 9600, plotLength = 100, dataNumBytes = 2):
        self.port = serialPort
        self.baud = serialBaud
        self.plotMaxLength = plotLength
        self.dataNumBytes = dataNumBytes
        self.rawData = bytearray(dataNumBytes)
        self.data = collections.deque([0] * plotLength, maxlen=plotLength)
        self.isRun = True
        self.isReceiving = False
        self.thread = None
        self.plotTimer = 0
        self.previousTimer = 0



# plt.axis([0, 10, 0, 1])

# for i in range(100):
#     y = np.random.random()
#     plt.scatter(i, y)
#     plt.pause(0.05)

# plt.show()