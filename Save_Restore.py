#!/usr/bin/env python
# coding=utf-8
#TensorFlow技术解析与实战P79页

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import os

# This shows how to save/restore your model (trained variables).
# To see how it works, please stop this program during training and resart.
# This network is the same as 3_net.py

def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))


def model(X, w_h, w_h2, w_o, p_keep_input, p_keep_hidden): # this network is the same as the previous one except with an extra hidden layer + dropout
    X = tf.nn.dropout(X, p_keep_input)
    h = tf.nn.relu(tf.matmul(X, w_h))

    h = tf.nn.dropout(h, p_keep_hidden)
    h2 = tf.nn.relu(tf.matmul(h, w_h2))

    h2 = tf.nn.dropout(h2, p_keep_hidden)

    return tf.matmul(h2, w_o)


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels

X = tf.placeholder("float", [None, 784])
Y = tf.placeholder("float", [None, 10])

w_h = init_weights([784, 625])
w_h2 = init_weights([625, 625])
w_o = init_weights([625, 10])

p_keep_input = tf.placeholder("float")
p_keep_hidden = tf.placeholder("float")
py_x = model(X, w_h, w_h2, w_o, p_keep_input, p_keep_hidden)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=py_x, labels=Y))
train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)
predict_op = tf.argmax(py_x, 1)




# 在当前路径下定义一个ckpt_dir目录
ckpt_dir = "./ckpt_dir"
if not os.path.exists(ckpt_dir):
    os.makedirs(ckpt_dir)

# 定义一个计数器,为训练轮数计数
global_step = tf.Variable(0, name='global_step', trainable=False)

#保存和提取变量：tf.train.Saver()
# Call this after declaring all tf.Variables.
saver = tf.train.Saver()

# This variable won't be stored, since it is declared after tf.train.Saver()
non_storable_variable = tf.Variable(777)

# 训练并存储模型
# Launch the graph in a session
with tf.Session() as sess:
    # you need to initialize all variables
    tf.initialize_all_variables().run()

    # ckpt = tf.train.get_checkpoint_state(ckpt_dir)
    # if ckpt and ckpt.model_checkpoint_path:
    #     print(ckpt.model_checkpoint_path)
    #
    #     # 加载所有的参数
    #     saver.restore(sess, ckpt.model_checkpoint_path) # restore all variables
    #     # 可以直接使用模型进行预测,或者继续训练


    start = global_step.eval() # get last global_step
    print("Start from:", start)

    for i in range(start, 10):
        for start, end in zip(range(0, len(trX), 128), range(128, len(trX)+1, 128)):
            sess.run(train_op, feed_dict={X: trX[start:end], Y: trY[start:end],
                                          p_keep_input: 0.8, p_keep_hidden: 0.5})
        # 更新计数器
        global_step.assign(i).eval() # set and update(eval) global_step with index, i

        # 存储模型！
        saver.save(sess, ckpt_dir + "/model.ckpt", global_step=global_step)

        print(i, np.mean(np.argmax(teY, axis=1) ==
                         sess.run(predict_op, feed_dict={X: teX, 
                                                         p_keep_input: 1.0,
                                                         p_keep_hidden: 1.0})))


# 加载模型
with tf.Session() as sess:
    # you need to initialize all variables
    tf.initialize_all_variables().run()

    ckpt = tf.train.get_checkpoint_state(ckpt_dir)
    if ckpt and ckpt.model_checkpoint_path:
        print(ckpt.model_checkpoint_path)

        # 加载所有的参数
        saver.restore(sess, ckpt.model_checkpoint_path) # restore all variables
        # 可以直接使用模型进行预测,或者继续训练


# #图的存储与加载P82
# # 当仅保存图模型时，才将图写入二进制协议文件中，例如：
# v = tf.Variable(0, name='my_variable')
# sess = tf.Session()
# tf.train.write_graph(sess.graph_def, '/tmp/tfmodel', 'train.pbtxt')
# # 当读取时，又从协议文件中读取出来：
# with tf.Session() as _sess:
# with gfile.FastGFile("/tmp/tfmodel/train.pbtxt",'rb') as f:
# graph_def = tf.GraphDef()
# graph_def.ParseFromString(f.read())
# _sess.graph.as_default()
# tf.import_graph_def(graph_def, name='tfgraph')

