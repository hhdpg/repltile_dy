import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
w = tf.Variable([0], dtype = tf.float32, name = "w")
b = tf.Variable([0], dtype = tf.float32, name = "b")
x = tf.placeholder(tf.float32, name = "x")
linear_model = w * x + b
y = tf.placeholder(tf.float32,name = "y")
with tf.name_scope("loss-model"):
    loss = tf.reduce_sum(tf.square(linear_model - y))
    tf.summary.scalar("loss", loss)
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

#创建一个梯度下降优化器，学习效率为0.001
optimizer = tf.train.GradientDescentOptimizer(0.001)
meged = tf.summary.merge_all()
writer = tf.summary.FileWriter("/tmp/tensorflow", sess.graph)

train = optimizer.minimize(loss)
x_train = [1, 2, 3, 6, 8]
y_train = [4.8, 8.5, 10.4, 21.0, 25.3]
for i in range(10000):
    summary, _ = sess.run([meged, train], {x: x_train,y: y_train})
    writer.add_summary(summary, i)
curr_w, curr_b, curr_loss = sess.run([w, b, loss], {x: x_train,y: y_train})
print("w: %s b: %s loss: %s" % (curr_w, curr_b, curr_loss))