from bluepy import btle
from common import *
import struct
import os
from TCPClient import TCPNode
from myo import myo
import time
stat_count = 0
onArm = 0

def main():
	global onArm
	NODE_NUMBER = 1
	SERVER_IP = "172.29.61.75"
	
	
	per=btle.Peripheral("EF:CD:C9:EA:16:6C")
	def print_stat(msg):
		global stat_count
		global onArm
		stat_count += 1
		print(stat_count, "onarm", onArm, msg)

	
	
	myMyo = myo(per)
	def vibrate():
		print "server vibrate"	
		myMyo.vibrate(1)


	client = TCPNode(NODE_NUMBER, vibrate)
	client.connect(SERVER_IP,8000)
	client.send(onArm,213)
	class ScanDelegate(btle.DefaultDelegate):
		def __init__(self):
			btle.DefaultDelegate.__init__(self)
		def handleDiscovery(seld,dev,isNewDev,isNewData):
			pass

	class MyDelegate(btle.DefaultDelegate):
		def __init__(self,params):
			btle.DefaultDelegate.__init__(self)

		def handleNotification(self,cHandle,data):
			global onArm
			#print "Handle: %x" % cHandle
			if cHandle == 28:
				vals = unpack('10h',data)
				wxyz = vals[:4]
				acc = vals[4:7]
				gyro = vals[7:10]			

				print wxyz #"quat %i" % quat
				print acc #"acc %i" % acc
				print gyro #"gyro %i" % gyro
			elif cHandle == 0x23:
			
				#print "Pose detected"
				typ,val,xdir =unpack('3h',data)
				#print len(data)
				#print "Type: "
				#print typ
			
				if typ ==1 or typ == 3:
					print("hit this")
					onArm = 0
					client.send(onArm,get_rssi())
				
				elif typ == 2:
					print "Not On Arm"
					onArm = 2
					client.send(onArm,get_rssi())
				
				print_stat("Pose detected: " + typ)
							
			else:
				onArm = 0
				print ("Should never print #1 ", data)


	scanner = btle.Scanner().withDelegate(ScanDelegate())
	per.withDelegate(MyDelegate(None))

	queue = []
	def rssi_avg(rssi):
		queue.append(rssi)
		if queue.__len__() > 5:
			queue.pop(0)
		return sum(queue)/queue.__len__()	

	def add_rssi(rssi):
		queue.append(rssi)
		if queue.__len__() > 5:
			queue.pop(0)

	def get_rssi():
		if queue.__len__() == 0:
			return 9999
		return sum(queue)/queue.__len__()



	# enable EMG data
	#per.writeCharacteristic(0x28, bytearray([01,00]))
	#per.writeCharacteristic(0x19, bytearray([01,02,01,01]))
	#per.writeCharacteristic(0x19, pack('BBBBHBBBBB',2,9,2,1,C,emg_smooth,C // emg_hz, imu_hz,0,0))

	# enable IMU data
	per.writeCharacteristic(0x1d, bytearray([01,00]))

	#enable on/off arm notifications
	per.writeCharacteristic(0x24,bytearray([02,00]))
	per.writeCharacteristic(0x28,bytearray([02,00]))
	per.writeCharacteristic(0x19,bytearray([01,03,00,00,00]))
	per.writeCharacteristic(0x19,bytearray([01,03,00,00,01]))

	#C=1000
	#emg_hz=50
	#emg_smooth=100
	#imu_hz=50

	while True:
		#print "outside"	
		client.send(onArm,get_rssi())
		print_stat("True loop")
		#devices = scanner.scan()
		if per.waitForNotifications(1.0):
			print "Handling Notif..."
			#for dev in devices:
			#	print("found Device "+dev.addr)
			#	client.send(onArm,get_rssi()

if __name__ == "__main__":
	while True:
		global onArm
		onArm = 0
		try:
			main()
		except Exception as e:
			print "Main exception! ", e
			time.sleep(1)




			
