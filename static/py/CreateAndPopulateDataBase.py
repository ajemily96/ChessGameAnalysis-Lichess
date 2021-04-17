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
engine = create_engine("sqlite:///Resources/chessdatalichness.sqlite")

# reflect an existing database into a new model
Base = declarative_base()

# inspect DB to see what tables we have
inspector = inspect(engine)

# check out what tables exist
inspector.get_table_names()

# Creates Classes which will serve as the anchor points for our Tables
class CHESS_DATA(Base):
    __tablename__ = 'CHESS_DATA'
    game_id = Column(Integer, primary_key=True)
    rated = Column(String(5))
    created_at = Column(String(255))
    last_move = Column(Integer)
    turns = Column(Integer)
    victory_status = Column(String(255))
    increment_code = Column(String(255))
    white_id = Column(String(255))
    white_rating = Column(String(255))
    black_id = Column(String(255))
    black_rating = Column(String(255))
    Opening_Eco = Column(String(255))
    Opening_Name = Column(String(255))
    Opening_Ply = Column(String(255))

# Create (if not already in existence) the tables associated with our classes.
Base.metadata.create_all(engine)

# Create function for loading data
def Load_Data(file_name):
    data = np.genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

# open session
session = Session(engine)

# load the data from CSV
file_name = "CleanedData.csv" 
data = Load_Data(file_name) 

for i in data:
    record = CHESS_DATA(**{
        'game_id' : i[0],
        'rated' : i[1],
        'created_at' : i[2],
        'last_move' : i[3],
        'turns' : i[4],
        'victory_status' : i[5],
        'increment_code' : i[6],
        'white_id' : i[7],
        'white_rating' : i[8],
        'black_id' : i[9],
        'black_rating' : i[10],
        'Opening_Eco' : i[11],
        'Opening_Name' : i[12],
        'Opening_Ply' : i[13]
    })
    session.add(record) #Add all the records

session.commit() #Attempt to commit all the records

# query data from table
game_list = session.query(CHESS_DATA)
for game in game_list:
    print(game.game_id)

# close session
session.close()