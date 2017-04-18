# -*- coding: utf-8 -*-
import os
import time
import re
 
def CPU(app_name='',path='c:/'):

	def Log_file(data):
		try:
			print u'Generate data files...'
			tiems = time.strftime("%m%d-%H%M%S", time.localtime())
    		File = open( r'%s'%(path) + r'\CpuData%s.txt'%(tiems),'w' )
			for i in range(len(data)):
				File.write(str(data[i])+'\n')
			File.close()
			print u'Save the file successfully'
		except:
			print 'Save file failed'

	cut_formula = re.compile(r'\s+')

	#存放CPU数据的数组
	cpu_array = []
	
	try:
		#增加变量来控制找不到包名后不要过早报错
		p = 0
		#增加变量控制每10次循环检查一遍连接
		i = 0
		while 1>0:			
			
			if  i == 0:
				link = ''.join(os.popen('adb devices').readlines()[1])
				try:
	            	#表达式=-1说明没找到设备
					assert link.find('device')!=-1,u'error'
					#循环N次后检查连接
					i = 10
				except:
					print 'Equipment broken links'
					raise ValueError('Equipment broken linksd')
			#i 减到 0 检查一次连接		
			i = i - 1

			a = os.popen('adb shell top -m 80 -n 1 -s cpu').readlines()
			#print a
			for i in range(len(a)):
				if ''.join(a[i]).find('%s'%app_name) != -1 and ''.join(a[i]).find(':') == -1:
					b = ''.join(a[i])
					#print b
					#连接成功就重置控制变量P
					p = 0
					break
				# i 是从0开始的
				elif i == len(a)-1:	
					#重连5次后报错
					if p == 5:
						print('No app detected')
						raise ValueError('No app detected')
					else:
						p = p + 1
						print 'disconnect',p
			# re.sub(): b 中的 空格符 替换成“？” ，分割字符串 b
			#a    b c->a?b?c
			#a?b?c->['a','b','c']
			#print '1',b
			try:
				if  p == 0:
					b = ''.join(re.sub(cut_formula,'?', b)).split('?')
					#print '2',b
					for k in b:
						if k.find('%') != -1:
							k = re.match(r'\d+',k).group()
							cpu_array.append(k) 
							print k,'%'
			except:
				if p == 5:
					raise ValueError('b')
				else:
					p = p + 1
			time.sleep(1)
	except:
		print 'Device or file can not be found'
		Log_file(cpu_array)

if __name__ == '__main__':

	import sys,getopt
	opts, args = getopt.getopt(sys.argv[1:], "hp:t:c:d:l:")
	for op, value in opts:
		if op == '-p':
 		    #print value
 		    Name = value
 		if op == '-t':
 		    #print value
 		    T = value
 		if op == '-l':
 		    path1 = value + 'data_%s'%(str(time.strftime("%m%d", time.localtime())))
	try:
		os.makedirs('%s'%(path1))
	except:
		pass

	CPU(app_name = Name ,path = path1)
