import tensorflow as tf

stats = tf.constant([[1,2,3],[4,5,6]])
print(stats.numpy())
print(" ")
print(tf.reduce_max(stats, axis=1))
print(" ")
print(tf.reduce_sum(stats, axis=1))
