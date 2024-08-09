#
#

import psycopg2 as pg
import pandas as pd
import matplotlib.pyplot as plt

conn = pg.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "12345678",
                        port = 5432)

stmt = """SELECT Series_reference, PERIOD, max(Data_value) 
FROM CONSUMER_2024
WHERE PERIOD > 2011
GROUP BY PERIOD, Series_reference
ORDER BY PERIOD, Series_reference
;"""

'''
cur = conn.cursor()
cur.execute(stmt)
rows = cur.fetchall()
for row in rows:
    print(f"{row[0]}, {row[1]}, {row[2]}")
conn.close()
'''

df = pd.read_sql_query(stmt, con=conn, index_col='series_reference')
df.columns
df.head(2)
for i in df['period']:
    print(i)

fig, axs = plt.subplots(1, 1, layout='constrained')
period_ = df.groupby(df['period']).mean('data_value')
period_.plot(kind='pie', subplots=True) ; plt.show()

fig, axs = plt.subplots(figsize=(4, 1))
fig.savefig("no2_concentrations.png")
axs.grid(True)
period_.plot(kind='line', legend='reverse') ; plt.show()

