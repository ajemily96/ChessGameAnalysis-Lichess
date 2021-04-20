import numpy as np

import pandas as pd

import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
from sqlalchemy import Column, Integer, String, Float 

import datetime as dt

import matplotlib.pyplot as plt

# Database Setup
engine = create_engine("sqlite:///../../data/chessdatalichness.sqlite")

# reflect an existing database into a new model
Base = declarative_base()

# inspect DB to see what tables we have
inspector = inspect(engine)

# check out what tables exist
inspector.get_table_names()

# Creates Classes which will serve as the anchor points for our Tables
class CHESS_DATA(Base):
    __tablename__ = 'CHESS_DATA'


    id = Column(Integer, primary_key=True)
    format = Column(String(10))
    victory_status = Column(String(50))
    book_moves = Column(Integer)
    opening_name = Column(String(250))
    winner = Column(String(5))
    turns = Column(Integer)
    white_id = Column(String(10))
    white_rating = Column(Integer)
    black_id = Column(String(10))
    black_rating = Column(Integer)


# Create (if not already in existence) the tables associated with our classes.
Base.metadata.create_all(engine)

# Create function for loading data
def Load_Data(file_name):
    data = np.genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

# open session
session = Session(engine)

# load the data from CSV
file_name = "../../data/CleanedData.csv" 
data = Load_Data(file_name) 

for i in data:
    record = CHESS_DATA(**{
        'id' : i[0],
        'format' : i[1],
        'victory_status' : i[2],
        'book_moves' : i[3],
        'opening_name' : i[4],
        'winner' : i[5],
        'turns' : i[6],
        'white_id' : i[7],
        'white_rating' : i[8],
        'black_id' : i[9],
        'black_rating' : i[10]
    })
    session.add(record) #Add all the records

session.commit() #Attempt to commit all the records

# query data from table
game_list = session.query(CHESS_DATA)
for game in game_list:
    print(game.game_id)

# close session
session.close()