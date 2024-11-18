import pandas as pd

df = pd.read_csv('./files/Input.csv')

df_cleaned = df.dropna()

df_cleaned.to_csv('cleaned_file.csv', index=False)

df_cleaned.to_json('cleaned_file.json', orient='records', lines=True)

df_cleaned.to_xml('cleaned_file.xml', index=False)

avg_age = df['age'].mean()
min_age = df['age'].min()
max_age = df['age'].max()

print(df_cleaned.to_string())

print(f"Середній вік: {avg_age}")
print(f"Мінімальний вік: {min_age}")
print(f"Максимальний вік: {max_age}")