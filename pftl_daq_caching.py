import serial 
from time import sleep

class Device:
    def __init__(self, port):
        self.rsc = serial.Serial(port)
        self.serial_number = None
        sleep(1)
    
    def idn(self):        
        # i = b'General DAQ Device built by Uetke. v.1.2019\n'
        if self.serial_number != None:

            return print(f"The serial number was already stored and it is {self.serial_number}")
        
        self.rsc.write(b'IDN\n')
        self.serial_number = self.rsc.readline() 
        return self.serial_number


dev = Device('COM3') #<---- Remember to change the port
serial_number2 = dev.idn()
print(f'The device serial number is: {serial_number2}')

cached_serial = dev.idn()
print()