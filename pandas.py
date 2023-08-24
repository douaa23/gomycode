import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)


print("First three rows:")
print(df.head(3))

df = df.dropna()

name_score_df = df[['name', 'score']]
print("\nExtracted 'name' and 'score' columns:")
print(name_score_df)

new_row = pd.Series({'name': 'Suresh', 'score': 15.5, 'attempts': 1, 'qualify': 'yes'}, name='k')
df = df.append(new_row)

df = df.drop('attempts', axis=1)
6/
df['Success'] = (df['score'] > 10).astype(int)

print("\nFinal DataFrame:")
print(df)

df.to_csv('my_data.csv')
