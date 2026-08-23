# 广播
import numpy as np

# (1,4)和(4,1)的数组相乘，结果（4,4）
# (2,4)和(4,1)的数组相乘，结果报错
# (4,4)和(4,1)的数组相乘，结果（4,4）
array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)  

array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
array2 = np.array([[1], [2], [3], [4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)  


array1 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
array2 = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)  
