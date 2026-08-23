import pandas as pd

df = pd.read_csv('Pandas/deepseek_csv_20260823_c71d57.csv')

# print(df.mean(numeric_only=True))
# print(df.median(numeric_only=True))
# print(df.std(numeric_only=True))
# print(df.min(numeric_only=True))    
# print(df.max(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.count())

# print(df['Salary'].mean(numeric_only=True))
# print(df['Salary'].median(numeric_only=True))
# print(df['Salary'].std(numeric_only=True))
# print(df['Salary'].min(numeric_only=True))
# print(df['Salary'].max(numeric_only=True))
# print(df['Salary'].sum(numeric_only=True))
# print(df['Salary'].count())

group = df.groupby("Department")
print(group['Salary'].mean())  
print(group['Salary'].sum())