# This is a simple example on how to connect and read/write objects in Postgresql
#   Uses the native lib psycopg2 (but later on, a simple example with SQLAlchemy...)
# https://www.datacamp.com/tutorial/tutorial-postgresql-python

import psycopg2 as pg

conn = pg.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "12345678",
                        port = 5432)

# Creating a table
#  1 Open a cursor to perform database operations
cur = conn.cursor()
#  2 Execute a command: create datacamp_courses table
cur.execute("""CREATE TABLE datacamp_courses(
            course_id         SERIAL        PRIMARY KEY,
            course_name       VARCHAR (50)  UNIQUE NOT NULL,
            course_instructor VARCHAR (100) NOT NULL,
            topic             VARCHAR (20)  NOT NULL);
            """)
#  3 Make the changes to the database persistent
conn.commit()
#  4 Close cursor and communication with the database
cur.close()
#conn.close()


# 2 INSERT
cur = conn.cursor()
cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to SQL','Izzy Weber','Julia')");
cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Analyzing Survey Data in Python','EbunOluwa Andrew','Python')");
cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to ChatGPT','James Chapman','Theory')");
cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to Statistics in R','Maggie Matsui','R')");
cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Hypothesis Testing in Python','James Chapman','Python')");
conn.commit()
cur.close()
#conn.close()

# 3 SELECT simple version
cur = conn.cursor()
cur.execute('SELECT * FROM datacamp_courses;')
rows = cur.fetchall()
for row in rows:
    print(row)
#conn.close()

# 4 UPDATE simple version
cur = conn.cursor()
cur.execute("UPDATE datacamp_courses SET topic = 'SQL' WHERE course_name = 'Introduction to SQL';")
conn.commit()
#conn.close()

# 5 DELETE simple version
cur = conn.cursor()
cur.execute("DELETE from datacamp_courses WHERE course_name = 'Introduction to Statistics in R'");
conn.commit()
cur.close()

# 6 SELECT JOIN
cur = conn.cursor()
cur.execute("""SELECT course_name, course_instructor, topic, tiobe_ranking
FROM datacamp_courses
INNER JOIN programming_languages
ON datacamp_courses.topic = programming_languages.language_name""")
rows = cur.fetchall()
for row in rows:
    print(row)



# USING SqlAlchemy to connect to Postgresql DOESN'T WORK!!!
import sqlalchemy as db
engine = db.create_engine('postgresql://postgres:12345678@localhost:5432/postgres')
conn = engine.connect() 
output = conn.execute("SELECT * FROM datacamp_courses") # this seems to fail ???????
print(output.fetchall())
#conn.close()



cur.execute("select max(f3) from x1")
cur.execute("ROLLBACK")

cur.execute("SELECT f_x1_autofiller()") -- runs a function
cur.execute("COMMIT")

cur.execute("call p_x1_autofiller()") -- calls a procedure
cur.execute("COMMIT")

cur.fetchall()
cur.close()
conn.close()


cur.execute("call p_x1_autofiller()")