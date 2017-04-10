# -*- coding: utf-8 -*-
import re
#import pylab as pl
import os
import time
#
def Pss():
    T = 1800
    Name = 'com.tencent.qlauncher.lite'
    pss = []
    try:
        for jc in range(int(T)):
            link=''.join(os.popen('adb devices').readlines()[1])
            try:
                assert link.find('device') !=- 1,u'error'
            except:
                print '连接失败'
                break
            a=''.join(os.popen('adb shell dumpsys meminfo %s'%Name).readlines())
            #安卓7.0以下
            a=a.split('\r\n') 
            #安卓7.1
            #a=a.split('\n')
            for ck in a:
                if ck.find('TOTAL') != -1 and ck.find(':') == -1:
                    p=re.findall(r'\d+',ck)
                    print p[0]
                    pss.append(int(p[0]))
            print jc + 1
            time.sleep(0.44)
        print '录制完毕，正在处理...'
    except:
        print 'error'
    #x=range(0,len(pss))
    print '生成数据文件...'
    File = open('C:\\PssData.txt','w')
    for i in range(len(pss)):
        #File.write(str(x[i])+' '+str(pss[i])+'\n')
        File.write(str(pss[i])+'\n')
    File.close()
    
    print type(pss[0])
    print 'max:',max(pss)
    print 'min:',min(pss)
    avg = sum(pss) / len(pss)
    print 'average:',avg

    '''
    print '生成图表...'
    pl.xlabel('')
    pl.ylabel('P S S')
    pl.title('P S S Graphic')
    pl.plot(x,pss,'y')#这个是pss
    pl.show()
    '''

if __name__=='__main__':
    s = time.time()
    Pss()
    e = time.time()
    print 'time:',e-s