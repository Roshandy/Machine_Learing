# 算术
import numpy as np

# Scalar arithmetic 标量运算
array = np.array([1, 2, 3])

print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)


# Vector math funcs 向量数学函数
array = np.array([1.01, 2.25, 3.69])

print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))
print(np.exp(array))
print(np.log(array))
print(np.log10(array))
print(np.pi)

r = np.array([1, 2, 3])
print(np.pi * r ** 2)  # 圆面积公式


# Elementwise operations 元素级运算
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)


# Comparison operations 比较运算
scores = np.array([90, 85, 70, 60, 50])
print(scores > 80)
scores[scores < 60] = 0
print(scores)