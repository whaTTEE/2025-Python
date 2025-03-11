import tensorflow as tf

a = tf.constant([1,2,3], dtype='int32')
tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
tensor_3d.shape #TensorShape([2, 2, 2])
tensor_3d.ndim #ndim은 차원의 수를 나타냄 여기선 3차원
