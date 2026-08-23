import pandas as pd

df = pd.read_csv('Pandas/deepseek_csv_20260823_c71d57.csv',
                 index_col="Name")

print(df.to_string())

# print(df["Name"].to_string()) 
# print(df["Department"].to_string()) 
# print(df[["Name", "Department","Salary"]].to_string())

# print(df.loc["Alice Johnson"])
# print(df.loc["Alice Johnson":"Eve Wilson",["Department","Salary"]])
# print(df.iloc[0:3:2, 0:3])

person = input("Enter the name of the person you want to search for: ")

try:
    print(df.loc[person])
except KeyError:
    print(f"{person} not found.")