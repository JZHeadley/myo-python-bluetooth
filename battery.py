from bluepy import btle

battery_handle=0x0011

def get_battery(peripheral):
	"""
	returns the battery level of the myo
	"""
	return peripheral.readCharacteristic(battery_handle)
	

if __name__ == "__main__":
	per = btle.Peripheral("EF:CD:C9:EA:16:6C")
	print get_battery(per)
