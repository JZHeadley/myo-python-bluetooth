from bluepy import btle
from common import *
import struct
import os

class MyDelegate(btle.DefaultDelegate):
	def __init__(self,params):
		btle.DefaultDelegate.__init__(self)

	def handleNotification(self,cHandle,data):
		print "Handle: %x" % cHandle
		if cHandle == 28:
			vals = unpack('10h',data)
			quat = vals[:4]
			acc = vals[4:7]
			gyro = vals[7:10]
			
			print quat #"quat %i" % quat
			print acc #"acc %i" % acc
			print gyro #"gyro %i" % gyro
		elif cHandle == 36:
			typ, val, xdir = unpack('3B',data)
			print "got here into 36"			
			if typ == 1:
				print "On arm"
			elif typ == 2:
				print "Not On Arm"
			elif typ == 3:
				print "Some sort of pose?"
				print val
				print xdir
		else:
			print (data)
per=btle.Peripheral("EF:CD:C9:EA:16:6C")
per.withDelegate(MyDelegate(None))

# enable EMG data
per.writeCharacteristic(0x28, bytearray([01,00]))
per.writeCharacteristic(0x19, bytearray([01,02,01,01]))
#per.writeCharacteristic(0x2f, bytearray([01,00]))
#per.writeCharacteristic(0x2c, bytearray([01,00]))
#per.writeCharacteristic(0x32, bytearray([01,00]))
print per.readCharacteristic(0x28)
print per.readCharacteristic(0x35)
# enable IMU data
per.writeCharacteristic(0x1d, b'\x01\x00')
print per.readCharacteristic(0x1d)
print per.readCharacteristic(0x19)

C=1000
emg_hz=50
emg_smooth=100
imu_hz=50
per.writeCharacteristic(0x19, pack('BBBBHBBBBB',2,9,2,1,C,emg_smooth,C // emg_hz, imu_hz,0,0))
print per.readCharacteristic(0x19)

while True:
	if per.waitForNotifications(1.0):
		print "Handling Notif..."

	print "Waiting..."
	
