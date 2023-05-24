import pandas as pd

df = pd.read_csv('my_table.csv')

df['Год'] = pd.DatetimeIndex(df['Дата']).year
df['Месяц'] = pd.DatetimeIndex(df['Дата']).month
df['Квартал'] = pd.DatetimeIndex(df['Дата']).quarter

df['Номер + текст'] = df['Номер'].astype(str) + '_' + df['Текст']

df['Количество букв'] = df['Текст'].apply(len)

df['Количество Д'] = df['Текст'].str.lower().str.count('д')

df['Нижний регистр'] = df['Текст'].str.lower()

middle = df['Текст'].apply(lambda x: x[len(x)//2-1:len(x)//2+1])
df.insert(7, 'Средние буквы', middle)

df.to_csv('table_new.csv', index=False)