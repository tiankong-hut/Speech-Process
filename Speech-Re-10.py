# coding: utf-8
# python3.4中有tflearn
# tflearn: 为tensorflow提供的更高级的api的深度学习库
from __future__ import division, print_function, absolute_import
import tflearn
import speech_data

learning_rate = 0.0001
training_iters = 300000  # 迭代次数
batch_size = 64

width = 20       # MFCC特征
height = 80      # 最大发音长度
classes = 10     # 数字类别

#生成每一批MFCC语音*
batch = word_batch = speech_data.mfcc_batch_generator(batch_size)  #MFCC
X, Y = next(batch)

# train, test, _ = ,X
trainX, trainY = X, Y
testX, testY = X, Y #overfit for now

# Data preprocessing
# Sequence padding
# trainX = pad_sequences(trainX, maxlen=100, value=0.)
# testX = pad_sequences(testX, maxlen=100, value=0.)
# # Converting labels to binary vectors
# trainY = to_categorical(trainY, nb_classes=2)
# testY = to_categorical(testY, nb_classes=2)

# Network building： 定义网络模型
net = tflearn.input_data([None, width, height])
# net = tflearn.embedding(net, input_dim=10000, output_dim=128)
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, classes, activation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=learning_rate, loss='categorical_crossentropy')

# Training：训练模型
model = tflearn.DNN(net, tensorboard_verbose=0)   #可视化
model.load("tflearn.lstm.model")
while 1: #training_iters
  model.fit(trainX, trainY, n_epoch=100, validation_set=(testX, testY), show_metric=True,
          batch_size=batch_size)
  _y=model.predict(X)
model.save("tflearn.lstm.model")
print (_y)
print (y)


# 预测模型
# 输入一个语音文件，进行预测：
demo_file = "5_Vicki_260.wav"
demo=speech_data_.load_wav_file(speech_data.path + demo_file)
result=model.predict([demo])
result=numpy.argmax(result)
print("predicted digit for %s : result = %d " %(demo_file, result))

