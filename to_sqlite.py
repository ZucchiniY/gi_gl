import pandas as pd
from sqlalchemy import create_engine

column = [
    'Food Name', 'GI', 'Food Manufacturer', 'Product Category', 'Country',
    'Serving Size (g)', 'Carbs per serve (g)', 'GL', 'Reference',
    'Subject Types', 'Time Period', 'Subject No', 'Year Of Test', 'a'
]

df = pd.read_csv('gi2.csv',
                 sep='#',
                 encoding='utf-8',
                 index_col=None,
                 names=column)
engine = create_engine('sqlite:///gi.db', echo=True)
sqlite_connection = engine.connect()

sqlite_table = 'gi'
df.to_sql(sqlite_table, sqlite_connection, if_exists='fail', index=False)

sqlite_connection.close()
