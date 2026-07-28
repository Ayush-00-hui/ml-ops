import os
import pandas as pd
from sklearn.model_selection import train_test_split

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
raw_data_path = os.path.join(base_dir, 'data', 'raw.csv')

df = pd.read_csv(raw_data_path)

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Convert Yes/No to 1/0
df['Purchased'] = df['Purchased'].map({'Yes': 1, 'No': 0})

train, test = train_test_split(df, test_size=0.2, random_state=42)

train_path = os.path.join(base_dir, 'data', 'train.csv')
test_path = os.path.join(base_dir, 'data', 'test.csv')

train.to_csv(train_path, index=False)
test.to_csv(test_path, index=False)

print('Preprocessing completed.')
