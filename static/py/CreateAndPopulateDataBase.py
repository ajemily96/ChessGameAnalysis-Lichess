import numpy as np

import pandas as pd

import sqlalchemy
# from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine, func, inspect
from sqlalchemy import Table, Column, Integer, String, Float 
from sqlalchemy import MetaData
from sqlalchemy import insert

import datetime as dt

import matplotlib.pyplot as plt

# Database Setup
engine = create_engine("sqlite:///data/chessdatalichness.sqlite")

# reflect an existing database into a new model
Base = declarative_base()

#Create a metadata instance
metadata=MetaData(engine)

# open session
session = Session(engine)
# Session=sessionmaker(bind=engine)
# session=Session()

# Create the inspector and connect it to the engine
inspector = inspect(engine)

# check out what tables exist
inspector.get_table_names()

# Define structure of table
class CHESS_DATA():
    def __init__(self, id, format, victory_status, book_moves, opening_name, winner, turns, white_id, white_rating, black_id, black_rating):
        self.id = id 
        self.format = format
        self.victory_status = victory_status
        self.book_moves = book_moves
        self.opening_name = opening_name
        self.winner = winner
        self.turns = turns
        self.white_id = white_id
        self.white_rating = white_rating
        self.black_id = black_id
        self.black_rating = black_rating

# Create (if not already in existence) the tables associated with our classes.
Base.metadata.create_all(engine)
   
# Declaring a table 
Table('CHESS_DATA',metadata, 
Column('id', String(250), primary_key=True),
Column('format', String(250)),
Column('victory_status', String(250)),
Column('book_moves', Integer),
Column('opening_name', String(500)),
Column('winner', String(250)),
Column('turns', Integer),
Column('white_id', String(250)),
Column('white_rating', Integer),
Column('black_id', String(250)),
Column('black_rating', Integer)
)

# Create (if not already in existence) the tables associated with our classes.
Base.metadata.create_all(engine)

# inspect DB to see what tables we have
inspector = inspect(engine)

# # Create function for loading data
# def Load_Data(file_name):
#     data = np.genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
#     return data.tolist()

# load the data from CSV
file_name = "data/chess.csv" 
# data = Load_Data(file_name)
data = pd.read_csv(file_name) 

# for i in data:
#     conn = engine.connect()
#     ins = CHESS_DATA.insert().values( {'id':i[0], 'format' : i[1], 'victory_status' : i[2], 'book_moves' : i[3], 'opening_name' : i[4], 'winner' : i[5], 'turns' : i[6], 'white_id' : i[7], 'white_rating' : i[8], 'black_id' : i[9], 'black_rating' : i[10]})
#     conn.execute(ins)

for i in data:
    record = CHESS_DATA(id = i[0], format = i[1], victory_status = i[2], book_moves = i[3], opening_name = i[4], winner = i[5], turns = i[6], white_id = i[7], white_rating = i[8], black_id = i[9], black_rating = i[10])
    #Add all the records
    session.add(record)

#Attempt to commit all the records
session.commit() 

# # query data from table
# game_list = session.query(CHESS_DATA)
# for game in game_list:
#     print(game.game_id)

# close session
session.close()