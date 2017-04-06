# -*- coding: utf-8 -*-
import re
import pylab as pl
import os
import time
import gc
#
def Pss():
    #T=raw_input('输入次数（间隔1s），按回车开始：')
    #Name=raw_input('输入包名：')
    T = 300
    Name = 'com.tencent.qlauncher.lite'

    #数据统一存放列表
    pss=[]
    pass
    try:
        for jc in range(int(T)):
            #连接检查
            #readlines第0行是List of devices attached，第二行才是设备名称
            link=''.join(os.popen('adb devices').readlines()[1])
            try:
                #表达式=-1说明没找到设备
                assert link.find('device')!=-1,u'error'
            except:
                print '连接失败'
                break

            a=''.join(os.popen('adb shell dumpsys meminfo %s'%Name).readlines())
            
            #安卓7.0以下
            a=a.split('\r\n') 
            
            #安卓7.1
            #a=a.split('\n')

            for ck in a:
                #找到记录下来的 a 中 含有'TOTAL'和不含'：'的那一行，用正则把数值找出来，放进pss列表中
                #因为每一次命令中都会出现两个'TOTAL'，如果只找'TOTAL'会出现两个一样的数值
                if ck.find('TOTAL')!=-1 and ck.find(':')==-1:
                    p=re.findall(r'\d+',ck)
                    print p[0]
                    pss.append(int(p[0]))
            #清理a中的数据，准备下一次记录
            del a
            gc.collect()
            print jc+1
            #循环延迟
            time.sleep(1)

        print '录制完毕，正在处理...'
    except:
        print 'error'

    #生成一个跟pss列表一样多的x轴
    x=range(0,len(pss))

    print '生成数据文件...'
    File=open('C:\\PssData.txt','w')
    for i in range(len(pss)):
        #File.write(str(x[i])+' '+str(pss[i])+'\n')
        File.write(str(pss[i])+'\n')
    File.close()
    
    print type(pss[0])

    print 'max:',max(pss)

    print 'min:',min(pss)

    avg = sum(pss) / len(pss)
    print 'average:',avg

    print '生成图表...'
    pl.xlabel('')
    pl.ylabel('P S S')
    pl.title('P S S Graphic')
    pl.plot(x,pss,'y')#这个是pss
    pl.show()
    

if __name__=='__main__':
    time.sleep(90)
    Pss()