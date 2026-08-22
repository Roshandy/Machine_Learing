import numpy as np

array = np.array('A')
print(array)
print(array.ndim)

array = np.array(['A'])
print(array)
print(array.ndim)

array = np.array([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']])
print(array)
print(array.ndim)

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                  [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                  [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '0']]])

word = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]

print(array)
print(array[0][0][0])
print(array[0, 0, 0]) #更快
print(word)
print(array.ndim)
print(array.shape)

