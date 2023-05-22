import pandas as pd
df = pd.read_csv('copy.csv', on_bad_lines='skip')
df.head()
df_filled = df.fillna('null')
print(df_filled)