import tensorflow as tf
import pandas as pd
from sklearn.utils import shuffle
import numpy as np
from sklearn.metrics import f1_score

def get1hot(a):
    one_hot = []
    for i in range(len(a)):
        t = np.eye(2)[a.iloc[i]]
        one_hot.append(t[0])
    return one_hot
data_frame = pd.read_csv("processed_dataset.csv")
data_frame = shuffle(data_frame)

train = data_frame.iloc[0:-30]
test = data_frame.iloc[-30:-1]
train_x = train.iloc[:, 1:6]

train_y = train.iloc[:, -1:]
train_y_1 = get1hot(train_y)

print len(train_y) == len(train_y)

test_x = test.iloc[:, 1:6]
test_y = test.iloc[:, -1:]
test_y_1 = get1hot(test_y)

print len(test_y) == len(test_y)

input_features = len(train_x.iloc[0])
hidden_nodes1 = 10
hidden_nodes2 = 20
output_classes = len(train_y_1[0])


X = tf.placeholder(tf.float32, shape=[None, input_features], name='XXX')
Y = tf.placeholder(tf.float32, shape=[None, output_classes], name="YYY")
w1 = tf.Variable(tf.random_normal([input_features, hidden_nodes1]))
b1 = tf.Variable(tf.random_normal([hidden_nodes1]))
l1_out = tf.nn.softmax(tf.matmul(X, w1) + b1)


w2 = tf.Variable(tf.random_normal([hidden_nodes1, hidden_nodes2]))
b2 = tf.Variable(tf.random_normal([hidden_nodes2]))
l2_out = tf.nn.softmax(tf.matmul(l1_out, w2) + b2)


w3 = tf.Variable(tf.random_normal([hidden_nodes2, output_classes]))
b3 = tf.Variable(tf.random_normal([output_classes]))
y = tf.nn.softmax(tf.matmul(l2_out, w3) + b3)
y_max = tf.argmax(y, 1)


cross_entropy = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(y), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.005).minimize(cross_entropy)


sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
epochs = 2000
for i in range(epochs):
    sess.run(train_step, feed_dict={X: train_x, Y: train_y_1})
    # print "{} / {} done".format(i, epochs)
# print sess.run(Y_)
correct_prediction = tf.equal(tf.argmax(Y, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run([w1, w2, accuracy], feed_dict={X: test_x, Y: test_y_1}))


def predict(i1, i2, i3, i4, i5):
    return sess.run(y, feed_dict={X: [[i1, i2, i3, i4, i5]]})

print predict(0.8615384615,0.4792703151,1,0.9651162791,0.7487437186)
print predict(0.7384615385,0.2985074627,1,0.9651162791,0.2825613215)