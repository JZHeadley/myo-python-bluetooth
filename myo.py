
class myo(object):

    # Static variables of the myohw header file
    myohw_command_t = 0x0019
    battery_handle=0x0011

    def __init__(self, peripheral):
        """
        The user must input their own peripheral (e.g. bluepy.btle.Preipheral(`MAC_Adress`))
        The battery is set to None by default and is calculated by a property method
        """
        self.peripheral = peripheral


    @property
    def battery(self):
	    """
	    returns the battery level of the myo
	    """
	    return ord(self.peripheral.readCharacteristic(myo.battery_handle))

    @property
    def firmware_version(self):
	"""
	returns the current version of the firmware on the myo
	"""
	print self.peripheral.readCharacteristic(0x17)    

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
    from bluepy import btle

    per = btle.Peripheral("EF:CD:C9:EA:16:6C")
    m = myo(per)
    m.vibrate(3)
    print(m.battery)
    m.firmware_version()
