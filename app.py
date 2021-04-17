# import dependencies
import os
import sqlalchemy
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, request, render_template, redirect

# database setup
path="data/chessdatalichness.sqlite"
engine=create_engine(f"sqlite:///{path}")


# create flask app
app=Flask(__name__)
# ignore key sort
app.config['JSON_SORT_KEYS'] = False


# set 'Home' route 
@app.route("/")
#create function that tells the server when user has entered home page
def home():
    print("Server has recieved request for 'Welcome' page...")
    
    # return f"error! Please input proper api path",404
    return render_template("index.html")

# set up route for API documentation
@app.route("/api-documentation")
def api_doc():
    return render_template("api.html")

# route for full data set
@app.route("/api/v1.0/chess")
def earthquake_db():
    results_list=[]
    results=engine.execute("SELECT * FROM CHESS")
    
    for result in results:
        results_list.append(result)
    
    json_dict={"data":[]}
    
    for game_id, rated, created_at, last_move, turns, victory_status, increment_code, white_id, white_rating, black_id, black_rating, Opening_Eco, Opening_Name, Opening_Ply in results_list:
        test_dict={"properties":{}}
        
        test_dict["properties"]["game_id"]=game_id
        test_dict["properties"]["rated"]=rated
        test_dict["properties"]["created_at"]=created_at
        test_dict["properties"]["last_move"]=last_move
        test_dict["properties"]["turns"]=turns
        test_dict["properties"]["victory_status"]=victory_status
        test_dict["properties"]["increment_code"]=increment_code
        test_dict["properties"]["white_id"]=white_id
        test_dict["properties"]["white_rating"]=white_rating
        test_dict["properties"]["black_id"]=black_id
        test_dict["properties"]["black_rating"]=black_rating
        test_dict["properties"]["Opening_Eco"]=Opening_Eco
        test_dict["properties"]["Opening_Name"]=Opening_Name
        test_dict["properties"]["Opening_Ply"]=Opening_Ply

        json_dict["data"].append(test_dict)

    return jsonify(json_dict)


    
#close out flask
if __name__=='__main__':
    app.run(debug=True)
