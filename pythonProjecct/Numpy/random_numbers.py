import numpy as np

rng = np.random.default_rng(seed=1)

# print(rng.integers(1,101, size=(3,4)))

# print(np.random.uniform(-1, 1, size=(3, 4)))

# array = np.array([1, 2, 3, 4, 5])
# rng.shuffle(array)
# print(array)

fruits = np.array(['apple', 'banana', 'cherry', 'date', 'elderberry'])
fruit = rng.choice(fruits, size=(3, 3))  # Randomly select 3 unique fruits
print(fruit)