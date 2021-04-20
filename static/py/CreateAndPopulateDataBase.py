import sqlite3 
import pandas as pd 

# Database Setup
conn = sqlite3.connect(r'data/chessdatalichness.sqlite')

# Load the data from CSV
file_name = "data/chess.csv" 
data = pd.read_csv(file_name)

# Load to the DB, replace if exists
data.to_sql('CHESS_DATA', conn, if_exists='replace', index = False)

# Create a cursor object 
cur = conn.cursor() 

# Fetch and display result 
count = cur.execute('SELECT COUNT(id) FROM CHESS_DATA')
print(count.fetchone())
