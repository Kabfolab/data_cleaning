import pandas as pd

# 1. Load
df = pd.read_csv("donations.csv")
print("Before:", df.shape)
print(df.isnull().sum())

# 2. Clean
df = df.dropna(subset=['email'])
df['name'] = df['name'].str.title()
df['email'] = df['email'].str.lower()
df = df.drop_duplicates(subset=['email'])
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df[(df['amount'] > 0) & (df['amount'] < 100000)]

# 3. Save
df.to_csv("cleaned_donations.csv", index=False)
print("After:", df.shape)
print("Done! File saved as cleaned_donations.csv")
