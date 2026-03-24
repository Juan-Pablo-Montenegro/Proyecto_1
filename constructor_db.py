import pandas as pd
import sqlite3

df = pd.read_csv("exoplanetas.csv")
df = df.dropna()
df = df.groupby('pl_name', as_index=False).median()

conn = sqlite3.connect("datos_mision.db")

df.to_sql("tabla", conn, if_exists="replace", index=False)

conn.close()
