import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
w = tf.Variable([.1], dtype = tf.float32)
b = tf.Variable([-.1], dtype = tf.float32)
x = tf.placeholder(tf.float32)
linear_model = w * x + b
y = tf.placeholder(tf.float32)
loss = tf.reduce_sum(tf.square(linear_model - y))
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

#创建一个梯度下降优化器，学习效率为0.001
optimizer = tf.train.GradientDescentOptimizer(0.001)
train = optimizer.minimize(loss)
x_train = [1, 2, 3, 6, 8]
y_train = [4.8, 8.5, 10.4, 21.0, 25.3]
for i in range(10000):
    sess.run(train, {x: x_train,y: y_train})
print("w: %s b: %s loss: %s" % (sess.run(w), sess.run(b), sess.run(loss, {x: x_train, y: y_train})))