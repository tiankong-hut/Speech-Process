# coding=utf-8   #放在文字之前
# http://blog.csdn.net/c602273091/article/details/46502527
# http://blog.csdn.net/xsc_c/article/details/8944077
# http://blog.csdn.net/safenli/article/details/49388181
# PyAudio：使用这个可以进行录音、播放、生成wav文件等等

# # 一，播放声音
# #引入库
# import pyaudio
# import  wave
# # import  sys
#
# #定义数据流块
# CHUNK = 1024
# # if len(sys.argv) < 2:
# #     print("Plays a wave file. \n\nUsage: %s filename.wav" % sys.argv[0])
#     # sys.exit(-1)              #有问题，报错
#
# #只读方式打开WAV文件
# wf = wave.open(r"/home/chuwei/PycharmProjects/Neural network/陌上花早.wav",'rb')  #(sys.argv[1],'rb')
#
# p = pyaudio.PyAudio()
#
# #打开数据流
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(), rate=wf.getframerate(),
#                 output=True)
#                  #format 取样值的量化格式
# #读取数据流
# data = wf.readframes(CHUNK)
#
# #播放
# while data != '':
#     stream.write(data)               #从wf中读数据，然后写到stream中,就是从文件中读取数据然后写到声卡里.
#     data = wf.readframes(CHUNK)      #从音频流中读取CHUNK个采样数据
#
#停止数据流
# stream.stop_stream()
# stream.close()
#
# #关闭 Pyaudio
# p.terminate()


# # 二，录音
# import pyaudio, wave
#
# CHUNK = 1024
# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "output.wav"
#
# p = pyaudio.PyAudio()
# stream = p.open(format=FORMAT, channels=CHANNELS,
#                 rate=RATE, input=True,
#                 frames_per_buffer=CHUNK)
# print("* recording")
#
# frames = []
#
# for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)
#
# print("* done recording")
#
# stream.stop_stream()
# stream.close()
# p.terminate()
#
# wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
# wf.setnchannels(CHANNELS)
# wf.setsampwidth(p.get_sample_size(FORMAT))
# wf.setframerate(RATE)
# wf.writeframes(b''.join(frames))
# wf.close()


# 三, 回放
# coding=utf-8
# https://www.2cto.com/kf/201305/212227.html

import pyaudio
import wave
import numpy as np

# define stream chunk
chunk = 1024

# open a wav format music
# f = wave.open(r"A2.wav", "rb")
f = wave.open(r"output.wav", "rb")

# instantiate PyAudio
p = pyaudio.PyAudio()
# open stream
stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                channels=f.getnchannels(),
                rate=f.getframerate(),
                output=True)
# read data
data = f.readframes(chunk)
# print data


# paly stream
while data != '':
    stream.write(data)
    data = f.readframes(chunk)

# stop stream
stream.stop_stream()
stream.close()

# close PyAudio
p.terminate()



# # 三，回放
# import pyaudio
#
# CHUNK = 1024
# WIDTH = 2
# CHANNELS = 2
# RATE = 44100
# RECORD_SECONDS = 5
#
# p = pyaudio.PyAudio()
# stream = p.open(format=p.get_format_from_width(WIDTH),
#                 channels=CHANNELS, rate=RATE,input=True,
#                 output=True, frames_per_buffer=CHUNK)
#
# print("* recording")
#
# for i in range(0, int(RATE/CHUNK*RECORD_SECONDS)):
#     data = stream.read(CHUNK)     #从数据流中读取采样数据
#     stream.write(data, CHUNK)     #写到数据流流中，从声卡播放。
#
# print("* done")
#
# stream.stop_stream()
# stream.close()
#
# p.terminate()





# http://blog.csdn.net/safenli/article/details/49388181
# 三.解析
# 通过wave模块从音频文件中读取数据，返回wave类。然后把读取的str数据通过pyaduio模块写到声卡里。
# 1. wave模块
# wf =wave.open(filenanme, mode’)此处读取音频文件，返回instance对象类
# 对wave类操作如下：
# wf.setnchannels(1) 设置音频文件的声道数，用在写音频流时
# wf.setsampwidth(2) 设置音频文件每个采样值得保存位数，用在写音频流时
# wf.setframerate(8000)设置采样率，用在写音频流时
# wf.getnchannels() 获得音频文件的声道数，用在读音频流时
# wf.getsampwidth() 获得音频文件每个采样值得保存位数，用在读音频流时
# wf.getframerate()获得采样率，用在读音频流时
# 2. pyaudio模块
# 通过p = pyaudio.PyAudio()返回pyaudio类instance，通过此类可以操作声音输出输入
# PyAudio类的open函数有许多参数：
# rate - 取样频率
# channels - 声道数
# format - 取样值的量化格式 (paFloat32, paInt32, paInt24, paInt16, paInt8 …)。在上面的例子中，使用 get_format_from_width方法将wf.sampwidth()的返回值2转换为paInt16
# input - 输入流标志，如果为True的话则开启输入流
# output - 输出流标志，如果为True的话则开启输出流
# input_device_index - 输入流所使用的设备的编号，如果不指定的话，则使用系统的缺省设备
# output_device_index - 输出流所使用的设备的编号，如果不指定的话，则使用系统的缺省设备
# frames_per_buffer - 底层的缓存的块的大小，底层的缓存由N个同样大小的块组成
# start - 指定是否立即开启输入输出流，缺省值为True
