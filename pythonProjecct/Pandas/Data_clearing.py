import pandas as pd

df = pd.read_csv('Pandas/deepseek_csv_20260823_c71d57.csv')

# 1. Drop irrelevant columns
# df =df.drop(columns=['HireDate', 'EmployeeID'])

# 2. Handle missing data
# df = df.dropna(subset=['Salary'])  # Drop rows with missing values in the 'Salary' column
df = df.fillna({'Salary': df['Salary'].mean()})  # Fill missing values in 'Salary' with the mean

# 3. Fix inconsistent values
# df['Department'] = df['Department'].replace(
#                 {"Engineering": "Eng", 
#                  "Human Resources": "HR",
#                  "Finance": "Fin",
#                  "Marketing": "Mktg"})

# 4. Standardize text
# df['Name'] = df['Name'].str.lower()
# df['Name'] = df['Name'].str.upper()
# df['Name'] = df['Name'].str.strip('i')

# 5. Fix data types
df['Salary'] = df['Salary'].astype(int)

# 6. Remove duplicates
df = df.drop_duplicates()

print(df)