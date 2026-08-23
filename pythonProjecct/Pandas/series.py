import pandas as pd

# data = [100.1, 102.2, 104.3, 106.4, 108.5]
# # data = ["A", "B", "C", "D", "E"]
# # data = [True, False, True, False, True]

# series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

# series.loc['a'] = 200.1

# print(series)
# print(series.loc['a'])
# print(series.iloc[0])
# print(series[series > 105])

calories = {"Day 1": 420, "Day 2": 380, "Day 3": 390}

series = pd.Series(calories)

# series.loc["Day 1"] += 450

print(series)
print(series.loc["Day 1"])
print(series[series > 400])