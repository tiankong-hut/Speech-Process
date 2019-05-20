# coding=utf-8
# a、为了使用PyAudio，首先使用 pyaudio.PyAudio()函数，来实例化PortAudio, 通过这个函数来建立portaudio系统
# b、为了录音或者播放音频，需要在设备上打开一个数据流，使用函数 pyaudio.PyAudio.open().
# 这样就可以建立一个 pyaudio.Stream 用来录音或者播放。


# # 录制wave
# #!/usr/bin/python
# import pyaudio,wave
#
# pa = pyaudio.PyAudio()
# stream = pa.open(format=pyaudio.paInt16,
#                  channels=1,
#                  rate=8000,
#                  input=True,
#                 frames_per_buffer=2000)
#
# save_buffer = ''
#
# wf = wave.open('haha.wav', 'wb')
# wf.setnchannels(1)
# wf.setsampwidth(2)
# wf.setframerate(8000)
# try:
#     while True:
#         string_audio_data = stream.read(1000)
#         save_buffer += string_audio_data
#         if len(save_buffer) >= 80000:#采样8次就保存
#             wf.writeframes(save_buffer)
#             break
# except:
#     wf.close()

# #播放声音
# import pyaudio
# import wave

# # define stream chunk
# chunk = 1024

# # open a wav format music
# f = wave.open(r"/home/chuwei/PycharmProjects/Neural network/陌上花早.wav", "rb")
# # instantiate PyAudio
# p = pyaudio.PyAudio()
# # open stream
# stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
#                 channels=f.getnchannels(),
#                 rate=f.getframerate(),
#                 output=True)
# # read data
# data = f.readframes(chunk)
#
# # paly stream
# while data != '':
#     stream.write(data)
#     data = f.readframes(chunk)
#
# # stop stream
# stream.stop_stream()
# stream.close()
#
# # close PyAudio
# p.terminate()