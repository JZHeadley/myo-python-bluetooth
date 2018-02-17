from bluepy.btle import Scanner, DefaultDelegate

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
while True:
	devices=scanner.scan(0.1)

	for dev in devices:
		if dev.addr == "EF:CD:C9:EA:16:6C".lower():
			print "RSSI: %s" % dev.rssi
#			print "Device %s (%s), RSSI=%d dB" % (dev.addr,dev.addrType,dev.rssi)
#			for (adtype,desc,value) in dev.getScanData():
#				print " %s = %s" % (desc,value) 
