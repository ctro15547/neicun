# -*- coding: utf-8 -*-
def APP_traffic(App_name):
	import re
	import os
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

if __name__ == '__main__':

	import time
	name = 'com.tencent.wh.ai.assistant'
	t = 60
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
	except:
		raise ValueError('error')
	print name
	print 'start!'
	a = APP_traffic(name)
	start_snd = float(a['tcp_snd']) / 1024
	start_rcv = float(a['tcp_rcv']) / 1024
	print 'start_tcp_snd: %.2f KB'%(start_snd)
	print 'start_tcp_rcv: %.2f KB'%(start_rcv)

	time.sleep(t)

	a = APP_traffic(name)
	end_snd = float(a['tcp_snd']) / 1024
	end_rcv = float(a['tcp_rcv']) / 1024
	print 'end_tcp_snd: %.2f KB'%(end_snd)
	print 'end_tcp_rcv: %.2f KB'%(end_rcv)
	print '**'*20
	print 'tcp_snd: %.2f KB'%(end_snd - start_snd)
	print 'tcp_rcv: %.2f KB'%(end_rcv - start_rcv)