# 英文数字语音识别
#coding=UTF-8
# 测试
# import tensorflow as tf
# hello=tf.constant('Hello,tensorflow!')
# sess=tf.Session()
# print (sess.run(hello))

# 1,定义输入数据并预处理数据
# 首先，需要将语音处理成能够读取的矩阵形式。这里面用到了梅尔频率倒谱系数(MFCC）特征向量
import tflearn             #python3可以用
#import speech_data
import  tensorflow as tf

learning_rate=0.0001
training_iters=300000  #迭代次数
batch_size=64

width=20               #MFCC特征
height=80              #最大发音长度
classes=10             #数字类别

batch = word_batch = speech_data.mfcc_batch_generator(batch_size)   # 生成每一批 MFCC 语音
X, Y = next(batch)
trainX, trainY = X, Y
testX, testY = X, Y

# 2,定义网络模型
# 用 tflearn 真是很简洁，只用 4 行代码就定广好了一个长短期记忆 LSTM 模型
net = tflearn.input_data([None, width, height])
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, classes, activation='softmax')
net = tflearn.regression(net,optimizer='adam', learning_rate=learning_rate,
       loss='categorical_crossentropy')

# 3,训练模型 p202





