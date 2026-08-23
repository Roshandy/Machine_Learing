import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10]])

# print(np.sum(array))  # 求和
# print(np.mean(array))  # 求平均值
# print(np.max(array))  # 求最大值
# print(np.min(array))  # 求最小值
# print(np.std(array))  # 求标准差
# print(np.var(array))  # 求方差
# print(np.argmax(array))  # 求最大值的索引
# print(np.argmin(array))  # 求最小值的索引

print(np.sum(array, axis=0))  # 按列求和
print(np.sum(array, axis=1))  # 按行求和