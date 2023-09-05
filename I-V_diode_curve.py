import serial
import matplotlib.pyplot as plt
from time import sleep


device = serial.Serial('COM3', 9800) #open a specific port that identifies the device
print('Opened Serial') 
sleep(0.5)
x = []
y = []
R = 1000.0
com = 'OUT:CH0:'
Vo = 3.3/1024
Vi = 3.3/4096
for i in range(0, 4095, 10):
    a = bytes(com + str(i), 'utf-8')
    device.write(a + b'\n') # send a command to the device, \n means that you stopped to send information, the b letter says to python to encode as a binary string
    answer = device.readline()# read the answer of the device
    device.write(b'IN:CH0:0\n')

    value = device.readline()
    #value = value[2:-3]
    print(value)
    I = (float(value)*Vo)/R
    x.append(float(answer)*Vi - float(value)*Vo)
    
    y.append(I)
   

plt.plot(x, y)
plt.title("I-V Diode")
plt.ylabel("Current(A)")
plt.xlabel("Voltage(mV)")

plt.show()
device.close()
print('Device closed')

