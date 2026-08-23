import pandas as pd

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

# df = pd.read_csv('Pandas/deepseek_csv_20260823_c71d57.csv')
df = pd.read_json('Pandas/deepseek_json_20260823_2b1503.json')

print(df.to_string())