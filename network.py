# coding=UTF-8       #用python2.7时才用
# http://python.jobbole.com/88041/
# 你需要定义 x = [1,3,6] 和 y = [1,1,1]。
# 由于图用 tf.Tensor 表示数据单元，你需要创建常量 Tensors：
import tensorflow as tf
x = tf.constant([1,3,6])
y = tf.constant([1,1,1])

# 现在你将定义操作单元：
import tensorflow as tf
x = tf.constant([1,3,6])
y = tf.constant([1,1,1])
op = tf.add(x,y)

# 你有了所有的图元素。现在你需要构建图：
import tensorflow as tf
my_graph = tf.Graph()
with my_graph.as_default():
     x = tf.constant([1, 3, 6])
     y = tf.constant([1, 1, 1])
     op = tf.add(x,y)

# tf.Session 对象封装了 Operation 对象的执行环境。Tensor 对象是被计算过的（从文档中）。
# 为了做到这些，我们需要在 Session 中定义哪个图将被使用到：
import tensorflow as tf   # 有问题
my_graph = tf.Graph()
with tf.Session(graph=my_graph) as sesss:
     x = tf.constant([1,3,6])
     y = tf.constant([1,1,1])
     op = tf.add(x,y)

# 为了执行操作，你需要使用方法 tf.Session.run()
import tensorflow as tf
my_graph = tf.Graph()
with tf.Session(graph=my_graph) as sess:
     x = tf.constant([1,3,6])
     y = tf.constant([1,1,1])
     op = tf.add(x,y)
     result = sess.run(fetches=op)
     print(result)
 # TensorFlow 的工作原理,机器学习算法+数据=预测模型
# 现在有了神经网络的数据流图。把我们所看到的都转换为代码，结果是：
#Network parameters
n_hidden_1 = 10  #1st layer number of features
n_hidden_2 = 5
total_words = 5  # ??
n_input = total_words #words in vocab
n_classes = 3   #categories: graphics,space and baseball
def multilayer_perceptron(input_tensor,weights,biases):     #输入，多层感知机
    layer_1_multiplication = tf.matmul(input_tensor,weights['h1'])
    layer_1_addition = tf.add(layer_1_multiplication,biases['b1'])
    layer_1_activation = tf.nn.relu(layer_1_addition)  #激活函数
# Hidden layer with RELU activation
    layer_2_multiplication = tf.matmul(layer_1_activation,weights['h2'])
    layer_2_addition = tf.add(layer_2_multiplication,biases['b2'])
    layer_2_activation = tf.nn.relu(layer_2_addidion)
# output layer with linear activation
    out_layer_multiplication = tf.matmul(layer_2_activation,weights['out'])
    out_layer_addition = out_layer_multiplication + biases['out']

    return out_layer_addition

# 权重和误差存储在变量（tf.Variable）中。这些变量通过调用 run() 保持在图中的状态。在机器学习中我们一般通过 正太分布 来启动权重和偏差值。
weights = {
     'h1': tf.Variable(tf.random_normal([n_input,n_hidden_1])),
     'h2': tf.Variable(tf.random_normal([n_hidden_1,n_hidden_2])),
     'out': tf.Variable(tf.random_normal([n_hidden_2,n_classes]))
    }
biases = {
     'b1': tf.Variable(tf.random_normal([n_hidden_1])),
     'b2': tf.Variable(tf.random_normal([n_hidden_2])),
     'out': tf.Variable(tf.random_normal([n_classes]))
    }

# 当我们第一次运行神经网络的时候（也就是说，权重值是由正态分布定义的）:
# input values: x
# weights: w
# bias: b
# output values: z
# expected values:expected

# 通过 TensorFlow 你将使用 tf.nn.softmax_cross_entropy_with_logits() 方法计算交叉熵误差（这个是 softmax 激活函数）并计算平均误差 (tf.reduced_mean())。
#construct model
# prediction = multilayer_perceptron(input_tensor,weights,biases)   #计算交叉熵误差
# #define loss
# entropy_loss = tf.nn.softmax_cross_entropy_with_logits(logits=prediction, ladels=output_tensor)
# loss = tf.reduce_mean(entropy_loss)   #计算平均误差

# 这个方法用新的值更新了所有的 tf.Variables ，因此我们不需要传递变量列表。现在你有了训练网络的代码：
# learning_rate = 0.001
# #construct model
# prediction = multilayer_perceptron(input_tensor,weights,biases)
# #define loss
# entropy_loss = tf.nn.softmax_cross_entropy_with_logits(logits=prediction,labels=output_tensor)
# loss = tf.reduce_mean(entropy_loss)
# optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)  #计算梯度下降

# # 将要使用的数据集有很多英文文本，我们需要操作这些数据将其传递给神经网络。
# import numpy as np   #numpy is a package for scientific computing
# from collection import Counter
# vocab = Counter
# text = "Hi from Brazil"
# vocab[word]+=1
# def get_word_2_index(vocab):
#      word2index = {}
#      for i,word in enumerate(vocab):
#           word2index[word] = i
#           return word2index
#      # Now we have an index
#      word2index = get_word_2_index(vocab)
#      total_words = len(vocab)
#      # This is how we create a numpy array (our matrix)
#      matrix = np.zeros((total_words), dtype=float)
#      # Now we fill the valuesfor word in text.split():
#      matrix[word2index[word]] += 1
#      print(matrix)





