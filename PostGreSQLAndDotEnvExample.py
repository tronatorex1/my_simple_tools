# This is an example on how to use postgres' psycopg2 library
#   Here dotenv seems not to read correctly the .env file, yet this is the way to use dotenv 

import dotenv, os
import psycopg2 as pg

dotenv.load_dotenv()
dbconn = os.getenv('DATABASE_URL')

# if dotenv does not work, fill the conn string with yhis
conn = pg.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "12345678",
                        port = 5432)

cur = conn.cursor()
cur.execute("select * from users;")
rows = cur.fetchall()
for row in rows:
    print(f"- {row[0]}")
conn.close()

# or 

cur = conn.cursor()
cur.execute("select * from users;")
for i in cur.fetchall():
    print(f" - {i[0]}")
cur.close()
conn.close()