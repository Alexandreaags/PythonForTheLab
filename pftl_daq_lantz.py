
from time import sleep
from lantz import MessageBasedDriver, Feat

class MyDevice(MessageBasedDriver):
    DEFAULTS = {'ASRL': {'write_termination': '\n',
    'read_termination': '\n',
    'encoding': 'ascii',
    }}
    output0 = None

    @Feat(limits=(0,4095,1))
    def set_output0(self):
        return self.output0
    @set_output0.setter

    def set_output0(self, value):
        command = "OUT:CH0:{}".format(value)
        self.write(command)
        self.output0 = value


    def idn(self): 
        return self.query('IDN')

    def get_analog_input(self, channel):
        message = 'IN:CH{}'.format(channel)
        ans = self.query(message)
        ans = int(ans)
        return ans
    
    

dev = MyDevice.via_serial('3')
dev.initialize()
print(dev.set_output0)
dev.set_output0 = 500
print(dev.set_output0)
sleep(1)
print(dev.idn)