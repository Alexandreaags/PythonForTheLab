import matplotlib.pyplot as plt
import serial 
from time import sleep


class Device:
    DEFAULTS = {'write_termination': '\n',
    'read_termination': '\n',
    'encoding': 'ascii',
    'baudrate': 9600,
    'read_timeout': 1,
    'write_timeout': 1,
    }


    def __init__(self, port):
        self.port = port
        self.rsc = None
        self.flag_check = False
    
    def initialize(self):
            self.rsc = serial.Serial(port=self.port,
                                baudrate=self.DEFAULTS['baudrate'],
                                timeout=self.DEFAULTS['read_timeout'],
                                write_timeout= self.DEFAULTS['write_timeout'])
            
            self.flag_check = True
            sleep(1)
    def finalize(self):
        if self.rsc is not None:
            print("Device Closed!")
            self.rsc.close()

    def idn(self): 
        return self.query('IDN')

    
    def get_analog_input(self, channel):
        message = 'IN:CH{}'.format(channel)
        ans = self.query(message)
        ans = int(ans)
        return ans
    
    def set_analog_output(self, channel, output_value):
        message = 'OUT:CH{}:{}'.format(channel, output_value)
        self.query(message)
    
    def query(self, message): # takes the message, append the proper termination, and encode it as specified in the DEFAULTS 
        if self.flag_check == True:
            message = message + self.DEFAULTS['write_termination']
            message = message.encode(self.DEFAULTS['encoding'])
            self.rsc.write(message)
            ans = self.rsc.readline()
            ans = ans.decode(self.DEFAULTS['encoding']).strip() #.strip() remove empty spaces of the string
            return ans
        else:
           print("Program not initialized!!")
           return exit()

    def linear_analog_out(self, start, step):
        stored_data = []
        bits = []
        for i in range(start, 4095, step):
            bits.append(i)
            self.set_analog_output(0, i)
            volts = (3.3*self.get_analog_input(0))/62
            print(f'Measured {volts}')
            stored_data.append(volts)
            sleep(.5)
            self.set_analog_output(0, 0)
            volts = (3.3*self.get_analog_input(0))/62
            print(f'Measured {volts}')
            sleep(.5)
            # stored_data.append(volts)
        plt.plot( bits, stored_data)
        plt.show()
        print(f"The values stored is {stored_data}")


dev = Device('COM3') #<---- Remember to change the port
dev.initialize()
serial_number = dev.idn()
print(f'The device serial number is: {serial_number}')
dev.linear_analog_out(2000, 200)

dev.finalize()