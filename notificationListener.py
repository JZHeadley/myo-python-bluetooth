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
			wxyz = vals[:4]
			acc = vals[4:7]
			gyro = vals[7:10]
			
			print wxyz #"quat %i" % quat
			print acc #"acc %i" % acc
			print gyro #"gyro %i" % gyro
		elif cHandle == 0x23:
			print "Pose detected"
			typ,val,xdir =unpack('3h',data)
			print len(data)
			print "Type: "
			print typ
			if typ == 1:
				print "On arm"
			elif typ == 2:
				print "Not On Arm"
			elif typ == 3:
				print "Some sort of pose?"
				print val
				print xdir
		elif cHandle == 39:
			#typ, val, xdir = unpack('3B',data)
			print "cHandle 27 data:"
			print data
			print unpack('17B', data)
			print len(data)
			"""
			typ = unpack('B',data)
			"""
		else:
			print (data)
per=btle.Peripheral("EF:CD:C9:EA:16:6C")
per.withDelegate(MyDelegate(None))

# enable EMG data
#per.writeCharacteristic(0x28, bytearray([01,00]))
#per.writeCharacteristic(0x19, bytearray([01,02,01,01]))

# enable IMU data
per.writeCharacteristic(0x1d, bytearray([01,00]))

#enable on/off arm notifications
per.writeCharacteristic(0x24,bytearray([02,00]))

per.writeCharacteristic(0x28,bytearray([02,00]))
#per.writeCharacteristic(0x19,bytearray([01,03,01,01,00]))
#per.writeCharacteristic(0x19,bytearray([01,03,01,01,01]))
per.writeCharacteristic(0x19,bytearray([01,03,00,00,00]))
per.writeCharacteristic(0x19,bytearray([01,03,00,00,01]))


C=1000
emg_hz=50
emg_smooth=100
imu_hz=50
#per.writeCharacteristic(0x19, pack('BBBBHBBBBB',2,9,2,1,C,emg_smooth,C // emg_hz, imu_hz,0,0))




while True:
	if per.waitForNotifications(1.0):
		print "Handling Notif..."

	print "Waiting..."
	
