# -*-coding: utf-8 -*-
import os
from uiautomator import Device
import subprocess
import time
import sys, getopt
def record_and_untied(b,x,y):
	#2000000
	child = subprocess.Popen('adb shell screenrecord --bit-rate 6000000 /sdcard/record%d.mp4'%(b))
	time.sleep(1)
	d.click(x, y)
	time.sleep(2)
	d.press("home")
	time.sleep(0.5)
	child.kill()
	child.wait()
	time.sleep(1)
	os.makedirs( r'%s'%(path1) + r'\jiezhen\%d'%(b))
	print 'mkdir-'*20
	child = subprocess.Popen(['adb','pull','sdcard/record%d.mp4'%(b), r'%s'%(path1) + r'\jiezhen\%d.mp4'%(b)])
	child.wait()	
	ffmpeg_path = os.path.split(os.path.realpath(__file__))[0] + '\\ffmpeg.exe'
	subprocess.Popen('%s'%(ffmpeg_path) + r' -i %s\jiezhen\%d.mp4 -f image2 -vf fps=fps=50 %s\jiezhen\%d'%(path1,b,path1,b)+r'/%d.jpg')
	if b == 3:
		time.sleep(7)
		sys.exit(0)
	else:
		child.wait()
if __name__ == '__main__':

	global path1
	
	opts, args = getopt.getopt(sys.argv[1:], "hp:t:c:d:l:")
	for op, value in opts:
		if op == '-c':
			X = int(value.split(',')[0])
			Y = int(value.split(',')[1])
		if op == '-d':
			#print value
			PHONE_ID = value
		if op == '-l':
			path1 = value

	d = Device(PHONE_ID)
	print X,Y
	print d.info
	try:
		os.makedirs( r'%s'%(path1) + r'\jiezhen')
	except:
		pass

	for k in xrange(1,4):
		record_and_untied(k, X, Y)