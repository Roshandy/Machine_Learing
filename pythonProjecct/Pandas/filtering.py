import pandas as pd

df = pd.read_csv('Pandas/deepseek_csv_20260823_c71d57.csv')

# highsalary = df[df['Salary'] > 60000.0]
# print(highsalary.to_string())

# fulltime = df[df['FullTime'] == True]
# print(fulltime.to_string())

H_F = df[(df['Salary'] > 80000.0) | 
         (df['FullTime'] == False)]
print(H_F.to_string())