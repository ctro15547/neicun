# -*- coding: utf-8 -*-
import re
import os
import time
def APP_traffic(App_name):
	if  App_name.find(':') != -1 or App_name.find('/') != -1:
		print 'error'
		raise ValueError('App_name error')
	a = os.popen('adb shell ps').readlines()
	lis = []
	for k in xrange(len(a)):
		if a[k].find('%s'%(App_name)) != -1 and a[k].find(':') == -1 and a[k].find('/') == -1:
			for x in a[k].split(' '):
				if  x != '':
					lis.append(x)
			Pid = lis[1]
			break        
	lis = []
	b = os.popen('adb shell cat /proc/%s/status'%(Pid)).readlines()
	for k in xrange(len(b)):
		if b[k].find('Uid:') != -1:
			for x in b[k].split('\t'):
				lis.append(x)
			Uid = lis[1]
			break
	#发送数据
	data = os.popen('adb shell cat /proc/uid_stat/%s/tcp_snd'%(Uid)).readlines()
	tcp_snd = re.findall(r'\d+',''.join(data[0]))
	#接收数据
	data = os.popen('adb shell cat /proc/uid_stat/%s/tcp_rcv'%(Uid)).readlines()
	tcp_rcv = re.findall(r'\d+',''.join(data[0]))
	data_dict = {	'tcp_snd':int(''.join(tcp_snd)),
					'tcp_rcv':int(''.join(tcp_rcv)),
					'Pid':Pid,
					'Uid':Uid    }
	return data_dict
def link():
	#Check the connection status
	link = ''.join(os.popen('adb devices').readlines()[1])
	#print link
	try:
		assert link.find('device') !=- 1,u'error'
	except:
		print 'off line'
		raise ValueError('off line')


if __name__ == '__main__':

	all_snd = []
	all_rcv = []

	name = 'com.tencent.tmgp.sgame'
	t = 600
	
	try:
		import sys,getopt
		opts, args = getopt.getopt(sys.argv[1:], "hp:t:c:d:l:")
		for op, value in opts:
			if op == '-p':
				#print value
				name = value
			if op == '-t':
				#print value
				t = value
			if op == '-l':
				path1 = value + 'data_%s'%( str(time.strftime("%m%d", time.localtime())))
	except:
		raise ValueError('error')
	
	try:
		os.makedirs('%s'%(path1))
	except:
		pass
	
	print name

	print 'start!'

	#Check the connection status
	link()

	a = APP_traffic(name)
	start_snd = float(a['tcp_snd']) / 1024
	start_rcv = float(a['tcp_rcv']) / 1024
	time.sleep(1)
	for T in range(int(t)):

		try:
			link()
		except:
			break

		print T+1
		a = APP_traffic(name)
		end_snd = float(a['tcp_snd']) / 1024
		end_rcv = float(a['tcp_rcv']) / 1024

		all_snd.append(float('%.2f'%(end_snd - start_snd)))
		all_rcv.append(float('%.2f'%(end_rcv - start_rcv)))

		print 'tcp_snd:' ,'%.2f'%(end_snd - start_snd) ,'KB'
		print 'tcp_rcv:' ,'%.2f'%(end_rcv - start_rcv) ,'KB'

		start_snd = end_snd 
		start_rcv = end_rcv

		time.sleep(0.5)

	print 'snd + ',sum(all_snd)
	print 'rcv + ',sum(all_rcv)
		
	print '生成数据文件...'
	tiems = time.strftime("%m%d-%H%M%S", time.localtime())
	File = open( r'%s'%(path2) + r'\Data_Flow_Data%s.txt'%(tiems),'w')
	#File = open( 'c:\Data_Flow_Data%s.txt'%(tiems) ,'w')
	File.write( 'SND' + ' ' + 'RCV' + '\n' )
	for i in range( len(all_snd) ):
		File.write( str(all_snd[i]) + ';' + str(all_rcv[i]) + '\n' )
	File.close()
