# This is INCOMPLETE example that explains how to access a PostGres' table (1, no join examples)
#   It only shows how to SELECT all records in a table and functions such as  DISTINCT, WHERE and ORDER BY

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
# Example: accessing users table
# engine=create_engine('postgresql://user:password@localhost:5432/database_name')
engine = create_engine('postgresql://postgres:12345678@localhost:5432/postgres')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
class User(Base):
    __tablename__ = 'users' # table's name
    id = Column(Integer, primary_key=True) # var must match table's col's name
    name = Column(String) # var must match table's col's name
    email = Column(String) # var must match table's col's name
    age = Column(Integer) # var must match table's col's name
users = session.query(User).all()
for user in users: # users is a cursor...
    print(user.id, user.name, user.email, user.age)
"""

# accesing people1 table
engine = create_engine('postgresql://postgres:12345678@localhost:5432/postgres') # conn var
Session = sessionmaker(bind=engine) # create session
session = Session()
Base = declarative_base() # open session
class p(Base):
    __tablename__ = 'people1'
    user_id = Column(String, primary_key=True) # var must match table's col's name (eg. var user_id == col user_id)
    job_title = Column(String) # var must match table's col's name
peoples = session.query(p).all()
for x in peoples:
    print(f"{x.user_id} | {x.job_title}")

peoples = session.query(p.user_id).all() # retrives only 1 col
for x in peoples:
  print(x.user_id)

peoples = session.query(p.user_id).order_by(p.user_id).all() # retrives only 1 col and sorts it out by same col
for x in peoples:
  print(x.user_id)

peoples = session.query(p.user_id).distinct(p.user_id).all() # retrives only 1 col and sorts it out by same col
for x in peoples:
  print(x.user_id)

peoples = session.query(p.user_id).filter(p.user_id == 'fffFEF2e8FEa873').all() # retrives only 1 col and sorts it out by same col
for x in peoples:
  print(x.user_id)


# accesing people1 JOIN people2 tables (INCOMPLETE TUTORIAL: no excplanation on how to exe joins)
engine = create_engine('postgresql://postgres:12345678@localhost:5432/postgres') # conn var
Session = sessionmaker(bind=engine) # create session
session = Session()
Base = declarative_base() # open session

class p1(Base):
    __tablename__ = 'people1'
    user_id = Column(String, primary_key=True) # var must match table's col's name (eg. var user_id == col user_id)
    job_title = Column(String) # var must match table's col's name

class p2(Base):
    __tablename__ = 'people2'
    user_id = Column(String, primary_key=True) # var must match table's col's name (eg. var user_id == col user_id)
    first_name = Column(String) # var must match table's col's name
    last_name = Column(String) # var must match table's col's name


peoples = session.query(p1, p2).all()
for x in peoples:
    print(f"{x.user_id} | {x.job_title}")



# Creating tables from SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
class Table1(Base):
    __tablename__ = "table1"
    id = Column(Integer, primary_key=True)
    column = Column(String, ForeignKey("table2.column2"))
    table2 = relationship("Table2")
class Table2(Base):
    __tablename__ = "table2"
    id = Column(Integer, primary_key=True)
    column2 = Column(String)

# session.close()
session.close_all()