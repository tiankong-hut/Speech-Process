# coding=UTF-8
# https://www.2cto.com/kf/201305/212227.html

import pyaudio
import wave
import struct

# define stream chunk
chunk = 1024

# open a wav format music
# f = wave.open(r"A2.wav", "rb")
f = wave.open(r"out2.wav", "rb")

# instantiate PyAudio
p = pyaudio.PyAudio()
# open stream
stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                channels=f.getnchannels(),
                rate=f.getframerate(),           #framerate帧速率:44100?
                output=True)

# read data
data = f.readframes(chunk)
# print data


# paly stream
while data != '':
    stream.write(data)                    #将数据写入数据流中
    data = f.readframes(chunk)            #从数据流中读出来

    # print ("data is %s" % repr(data))   #不用repr会乱码,repr()返回一个对象的 string 格式。
    # print ('length:', len(data))        #字符串长度为4096

    data = data[0:4]
    print ('length:', len(data))
    data1 = struct.unpack("i", data)   #格式符"i"表示转换为int，'ii'表示有两个int变量。 参数:长度为4的字符串
    print repr(data1)


# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()



# import wave
# import struct
# from scipy import *
# from pylab import *
#
# # 读取wav文件，我这儿读了个自己用python写的音阶的wav
# filename = 'output.wav'
# wavefile = wave.open(filename, 'r')  # open for writing
#
# # 读取wav文件的四种信息的函数。期中numframes表示一共读取了几个frames，在后面要用到滴。
# nchannels = wavefile.getnchannels()
# sample_width = wavefile.getsampwidth()
# framerate = wavefile.getframerate()
# numframes = wavefile.getnframes()      #表示一共读取了几个frames
#
# print("channel", nchannels)
# print("sample_width", sample_width)
# print("framerate", framerate)
# print("numframes", numframes)
