# This is a script that merely attempts to explain how to use sqlalchemy with postgres db
#   It seems not to work right with update() and other features...
# https://coderpad.io/blog/development/sqlalchemy-with-postgresql/

from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="12345678",
    host="localhost",
    port="5432",
    database="postgres"
)
engine = create_engine(url) # creates a conn obj, it has not yet connected to the db
connection = engine.connect() # connects to the db 

# Define a table to use
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime
Base = declarative_base()
class users(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False)
    age = Column(Integer())
# users.__table__

# Access/Select the table's contents
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
res = session.query(users).order_by(users.age.desc())
for x in res:
    print(x.id, x.name, x.email, x.age)

queries = session.query(users)
queries.first().id


# Insert new rows in table
# 1 at a time 
new_user = users(id=4, name='d', email='d@x.com', age=99)
session.add(new_user)
session.commit()
session.flush()
# 2 many rows at once
new_users = [users(id=5, name='e', email='e@x.com', age=98), users(id=6, name='f', email='f@x.com', age=97)]
session.add_all(new_users)
session.commit()
session.flush()

# Update a row (assign is the easiest way ; update does not work!)
new_user.id
new_user.id = 999
session.commit()

all_users = session.query(users).filter(users.id == 999)
for x in all_users:
    print(x.id)

all_users = session.query(users)
upd_row = all_users.filter(users.id == 999).first() # cursor that points to row id == 999
upd_row.id
upd_row.id = 8888888 # sets id=888888
session.commit()

upd_row.id = 4 # back to id=4
session.commit()

all_users = session.query(users)
upd_rows = all_users.filter(users.id > 3)
for x in upd_rows:
    print(x.id)

# Close all sessions
session.close()
# session.close_all_sessions()