# This is an example on how to insert (massively) data into a postgresql DB
#   Uses Faker to produce names used to insert in the text field

import psycopg2, time
from faker import Faker


#establishing the connection
conn = psycopg2.connect(database="postgres", user='postgres', password='12345678', host='localhost', port= '5432')

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Creating the destination table...
'''
cre_stmt = """
CREATE TABLE X3 (
    F1 serial primary key,
    F2 TEXT,
    created_on timestamp default current_timestamp not null
);
"""
cursor.execute(cre_stmt)
'''

start_ = time.time()
#Populating the table
faker = Faker()
for i in range(20000):
    ins_stmt = f"INSERT INTO X3 (f2) VALUES ('{faker.name()}');"
    cursor.execute(ins_stmt)
    #time.sleep(0.15)
    #print(f" - sending then stmt to insert new data into X3 table!.......")

#Commit your changes in the database
conn.commit()
stop_ = time.time()
print(f" total time (secs) = {(stop_ - start_)}")

#Closing the connection
cursor.close()
conn.close()