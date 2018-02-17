from bluepy import btle
myohw_command_t=0x0019


def vibrate(peripheral,length):
	"""
	makes the given peripheral vibrate short medium or long period of time
	"""
	peripheral.writeCharacteristic(myohw_command_t,vibrate_t(length))	

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


if __name__ == "__main__":
	per = btle.Peripheral("EF:CD:C9:EA:16:6C")
	vibrate(per,3)
