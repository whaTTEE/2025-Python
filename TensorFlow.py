import tensorflow as tf

# (2, 3, 2) 크기의 3D 텐서 생성 (X=2, Y=3, Z=2)
tensor_3d = tf.constant([
    [[1, 2], [3, 4], [5, 6]],  # X=0 블록
    [[7, 8], [9, 10], [11, 12]]  # X=1 블록
])


print(tensor_3d[:, :, 0].numpy())  # Z=0인 값들만 가져오기
