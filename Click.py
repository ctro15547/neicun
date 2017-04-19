from uiautomator import Device
import time

try:
	import sys,getopt
	opts, args = getopt.getopt(sys.argv[1:], "hp:t:c:d:l:")
	for op, value in opts:
		if op == '-d':
			#print value
			Phone_ID = value
		if op == '-c':
			#print value
			s = value
except:
	raise ValueError('error')

d = Device(Phone_ID)
print d.info
#s = '683,263;home'
coordinate_list = s.split(';')
print coordinate_list
while 1 > 0:
	try:
		test = d.info
	except:
		print 'off line'
		break
	for coordinate in coordinate_list:
		if coordinate == 'back':
			print 'back'
			d.press("back")
			time.sleep(1.9)
		elif coordinate == 'home':
			print 'home'
			d.press("home")
			time.sleep(1.9)
		else:
			c = ''.join(coordinate).split(',')
			print 'click:',c[0],c[1]
			d.click(int(c[0]) ,int(c[1]))
			time.sleep(1.9)