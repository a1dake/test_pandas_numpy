import pandas as pd

df = pd.DataFrame({
    'Дата': ['2022-12-30', '2023-02-05', '2023-02-09', '2023-02-10'],
    'Текст': ['Заяц', 'Медведь', 'Волк', 'Гиппопотам'],
    'Номер': [653, 875, 1092, 176]
})

df.index = df.index + 1

df.to_csv('my_table.csv', index=True)