#Author:xiao luo
import tensorflow as tf
a = tf.constant([1,2,3])
b = tf.constant([4,5,6])
#矩阵拼接[[1,4],[2,5],[3,6]]
c = tf.stack([a,b],axis=1)#(3*2)
#矩阵分解
d = tf.unstack(c,axis=0)#[1,4]、[2,5]、[3,6]
e = tf.unstack(c,axis=1)#
print(c.get_shape())
with tf.Session() as sess:
    print(sess.run(c))
    print(sess.run(d))
    print(sess.run(e))