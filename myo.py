
from bluepy import btle

class myo(object):

    myohw_command_t = 0x0019
    battery_handle=0x0011

    def __init(self, peripheral):
        self.peripheral = peripheral
        self.battery = None

    @property
    def battery(self):
	    """
	    returns the battery level of the myo
	    """
	    return self.peripheral.readCharacteristic(myo.battery_handle)

    def vibrate(self,length):
	    """
	    makes the given peripheral vibrate short medium or long period of time
	    """
	    self.peripheral.writeCharacteristic(myo.myohw_command_t, myo.vibrate_t(length))	

    @staticmethod
    def vibrate_t(length):
        """
        returns bytearray of the command with time period
        """
        if length == 1:
            return bytearray([0x03,0x01,0x01])
            
        elif length == 2:
            return bytearray([0x03,0x01,0x02])
            
        elif length == 3:
            return bytearray([0x03,0x01,0x03])
            
        else:
            return bytearray([0x03,0x01,0x00])


if __name__ == '__main__':
    per = btle.Peripheral("EF:CD:C9:EA:16:6C")
    m = myo(per)
    m.vibrate(3)
    print(m.battery
    