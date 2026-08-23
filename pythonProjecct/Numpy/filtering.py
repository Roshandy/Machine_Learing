import numpy as np

ages = np.array([[21, 17, 19, 20, 16, 40, 65, 50],
                 [15, 24, 88, 32, 18, 42, 48, 52]])

# teenagers = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages < 65)]
# senior_citizens = ages[ages >= 65]
# even_ages = ages[ages % 2 == 0]
# odd_ages = ages[ages % 2 == 1]

# print(teenagers)
# print(adults)
# print(senior_citizens)
# print(even_ages)
# print(odd_ages)

adults = np.where((ages >= 18) & (ages < 65), ages, 0)
print(adults)