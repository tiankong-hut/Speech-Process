# -*- coding: utf-8 -*-
#使用pyaudio + numpy + pylab 可视化音频的代码，下面的代码打开电脑的麦克风，然后接受音频输入，再以图像的形式展示出来。
#http://www.cnblogs.com/niansi/p/6854601.html
#PyAudio是一个功能强大的处理音频库
import pyaudio
import numpy as np
import pylab
import time

RATE = 44100    #采样频率
CHUNK = int(RATE/20)    # RATE/number of updates per second

def sound_plot(steam):  #画图
    t1 = time.time()    #返回当前时间的时间戳（1970纪元后经过的浮点秒数）
    data = np.fromstring(stream.read(CHUNK), dtype = np.int16)
    pylab.plot(data)
    pylab.title(i)
    pylab.grid()
    pylab.axis([0,len(data), -2**8, 2**8])
    pylab.savefig("sound.png", dpi=50)
    pylab.show(block = False)
    time.sleep(0.5)              #定时器Sleep定时秒及毫秒,让程序休眠
    # pylab.close('all')
    print("took %.2fms." %(time.time() - t1)*1000)

if __name__ == '__main__':
     p = pyaudio.PyAudio()
     stream = p.open(format = pyaudio.paInt16, channels = 1, rate = RATE,
              input = True,frames_per_buffer = CHUNK)
     for i in range(int(20 * RATE / CHUNK)):  #for 10 seconds
         sound_plot(stream)
     stream.stop_stream()
     stream.close()
     p.terminate()
