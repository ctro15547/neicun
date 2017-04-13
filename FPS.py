# -*- coding: utf-8 -*-
import re
#import pylab as pl
import os
import time
import gc

def Fps(T,Name,path2):
    print u"'请确保开发者选项中的'GPU呈现模式分析'调整正确"
    data = os.popen('adb shell getprop ro.build.version.release').readlines()
    version = re.findall(r'\d', ''.join(data))
    if int(version[0]) < 5:
        lv=3
        print lv
    else:
        lv=4
        print lv
    n=[]
    pass
    for jc in range(int(T)):
        link=''.join(os.popen('adb devices').readlines()[1])
        try:
            assert link.find('device')!=-1,u'error'
        except:
            print '连接失败'
            break
        print jc+1
        c=''
        a=''.join(os.popen('adb shell dumpsys gfxinfo %s'%Name).readlines())
        a=a.split('\r\n')
        for i in a:
            if i.lower().islower() == False:
                c=c+i+'\n'
        n.append(re.findall(r'\d+\.\d+',c))
        print n
        del a
        del c
        gc.collect()
        time.sleep(1.65)
    s=[]
    for m in n:
        for mm in m:
            s.append(mm)
    del n
    gc.collect()
    e=[]
    k=0
    for i in range(len(s)):
        if (i+1)%lv==0:
            k=k+float(s[i])
            e.append(float('%.2f'%k))
            k=0
        else:
            k=k+float(s[i])
    x=range(0,len(e))
    sta=[]
    for i in range(len(e)):
        sta.append(16)
    print '生成数据文件...'
    tiems = time.strftime("%m%d-%H%M%S", time.localtime())
    File = open( r'%s'%(path2) + r'\FpsData%s.txt'%(tiems),'w')
    for i in range(len(e)):
        File.write(str(x[i])+' '+str(e[i])+'\n')
    File.close()
    '''
    print '生成图表...'
    pl.xlabel('')
    pl.ylabel('F P S')
    pl.title('F P S Graphic')
    pl.plot(x,e,'y')#这个是FPS
    pl.plot(x,sta,'r')#这个是16ms线
    pl.show()
    '''
if __name__=='__main__':
    
    name =''
    t = ''
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp:t:c:d:l:")
        for op, value in opts:
            if op == '-p':
                #print value
                name = value
            if op == '-t':
                #print value
                t = value
            if op == '-l':
                path1 = value
    except:
        print 'error'
        name = 'com.taobao.idlefish' 
        t = 180
        raise ValueError('error')
    Fps(t,name,path1)