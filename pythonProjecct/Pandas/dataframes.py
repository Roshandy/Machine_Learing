import pandas as pd

data = {"Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 35, 40]}

df = pd.DataFrame(data, index=["Person 1", "Person 2", "Person 3", "Person 4"])

# add a new column to the DataFrame
df["Job"] = ["Engineer", "Doctor", "Artist", "Lawyer"]

# add a new row to the DataFrame
new_row = pd.DataFrame([{"Name": "Eve", "Age": 28, "Job": "Scientist"},
                       {"Name": "Kate", "Age": 45, "Job": "Manager"}],
                       index=["Person 5", "Person 6"])
df = pd.concat([df, new_row])

print(df)
print(df.loc["Person 1"])
print(df.iloc[0])