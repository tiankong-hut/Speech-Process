# coding=utf-8
# Python 读取WAV音频文件 画频谱
# struct模块的pack、unpack示例
# http://blog.csdn.net/daiyinger/article/details/48289575

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
#
# # 建一个y的数列，用来保存后面读的每个frame的amplitude。
# y = zeros(numframes)
#
# # for循环，readframe(1)每次读一个frame，取其前两位，是左声道的信息。右声道就是后两位啦。
# # unpack是struct里的一个函数，用法详见http://docs.python.org/library/struct.html。简单说来就是把＃packed的string转换成原来的数据，无论是什么样的数据都返回一个tuple。这里返回的是长度为一的一个
# # tuple，所以我们取它的第零位。
# for i in range(numframes):
#     val = wavefile.readframes(1)      #wavefile.readframes --
#     # print ("%s" % val)
#     left = val[0:2]
#     # print ("%s" % left)
#           # right = val[2:4]
#     v = struct.unpack('h', left)[0]
#     y[i] = v
#     print ("%s" % v)   #是数字
#
# # framerate就是44100，文件初读取的值。然后本程序最关键的一步！specgram！实在太简单了。。。
# Fs = framerate
# specgram(y, NFFT=1024, Fs=Fs, noverlap=900)
# show()


# http://blog.csdn.net/ithomer/article/details/5974029
# 1、 struct.pack
# Python只定义了六种基本类型：字符串，整数，浮点数，元组（set），列表（array），字典（key/value）
# struct.pack用于将Python的值根据格式符，转换为字符串,
# （因为Python中没有字节(Byte)类型， 可以把这里的字符串理解为字节流，或字节数组）。
# 其函数原型为：struct.pack(fmt, v1, v2, ...)，参数fmt是格式字符串，
# v1, v2, ...表示要转换的python值。
# 下面的例子将两个整数转换为字符串（字节流）:
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
#
# import struct
# a = 20
# b = 400
# str = struct.pack("ii", a, b)
# print 'length: ', len(str)   # length:  8
# print str                    # 乱码： �
# print repr(str)              # '\x14\x00\x00\x00\x90\x01\x00\x00'
# repr:repr() 函数将对象转化为供解释器读取的形式。 返回一个对象的 string 格式。
# 格式符"i"表示转换为int，'ii'表示有两个int变量。
# 进行转换后的结果长度为8个字节（int类型占用4个字节，两个int为8个字节）
# 可以看到输出的结果是乱码，因为结果是二进制数据，所以显示为乱码。
# 可以使用python的内置函数repr来获取可识别的字符串，
# 其中十六进制的0x00000014, 0x00001009分别表示20和400。

# 2、 struct.unpack
# struct.unpack做的工作刚好与struct.pack相反，用于将字节流转换成python数据类型。
# 它的函数原型为：struct.unpack(fmt, string)，该函数返回一个元组。
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
# import struct
# a = 20        #十六进制为0x0014 ，八进制：“O”
# b = 400       #十六进制为0x0190
# # # pack
# str = struct.pack("ii", a, b)
# # print 'length: ', len(str)     # length:  8 转化为字符串类型
# # print str                      # 乱码： 
# # print repr(str)                # '\x14\x00\x00\x00   \x90\x01\x00\x00'
# # unpack
# str2 = struct.unpack("ii", str)
# print 'length: ', len(str2)     # length:  2 ,转化为python类型
# print str2                      # (20, 400)
# print repr(str2)                # (20, 400)

# 3、 struct.calcsize
# struct.calcsize用于计算格式字符串所对应的结果的长度，如：struct.calcsize('ii')，返回8。
# 因为两个int类型所占用的长度是8个字节。
# import struct
# print "len: ", struct.calcsize('i')       # len:  4
# print "len: ", struct.calcsize('ii')      # len:  8
# print "len: ", struct.calcsize('f')       # len:  4
# print "len: ", struct.calcsize('ff')      # len:  8
# print "len: ", struct.calcsize('s')       # len:  1
# print "len: ", struct.calcsize('ss')      # len:  2
# print "len: ", struct.calcsize('d')       # len:  8
# print "len: ", struct.calcsize('dd')      # len:  16







# print ("He is %d years old" % 23)

# -*- coding: utf-8 -*-
# #import scipy
# from matplotlib.pyplot import specgram
# from scipy.io import wavfile
# sample_rate, X = wavfile.read('output.wav')
# print (sample_rate, X.shape)
# specgram(X, Fs=sample_rate, xextent=(0,192000))


