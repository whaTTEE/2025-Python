import tensorflow as tf

A = tf.constant([[1,2,3],[4,5,6]])
B = tf.fill((3,2), 2)
print(tf.matmul(A,B))

#matmul 함수는 TensorFlow에서 행렬 곱셈을 수행하는 함수
