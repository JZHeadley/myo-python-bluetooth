from bluepy.btle import Scanner, DefaultDelegate
import math

class ScanDelegate(DefaultDelegate):
	def __init__(self):
		DefaultDelegate.__init__(self)

	def handleDiscovery(self,dev,isNewDev,isNewData):
		"""
		if isNewDev:
			print "Discovered device", dev.addr
		elif isNewData:
			print "Received new data from", dev.addr
		"""

scanner = Scanner().withDelegate(ScanDelegate())

queue = []

def rssi_avg(rssi):
	queue.append(rssi)
	if queue.__len__() > 5:
		queue.pop(0)
	return sum(queue)/queue.__len__()

while True:
	devices=scanner.scan(0.1)

	for dev in devices:
		if dev.addr == "EF:CD:C9:EA:16:6C".lower():
			rssi = rssi_avg(dev.rssi)
			print "RSSI: %s" % rssi
#			print "Device %s (%s), RSSI=%d dB" % (dev.addr,dev.addrType,rssi)
#			for (adtype,desc,value) in dev.getScanData():
#				print " %s = %s" % (desc,value) 
