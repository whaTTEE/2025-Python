import tensorflow as tf

tensor_3d = tf.constant([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
tensor_3d[1,0,0].numpy() #1batch, 0행 0열이라는 뜻, 두 번째에 있는 레이어의 첫 번째 값 >> 5가 출력
