
# Import the Panda dependencies
import numpy as np
import pandas as pd

# Import the sql alchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect, desc

# Import flask and jsonify dependencies
from flask import Flask, jsonify

# Input the route to the data SQL file
engine = create_engine("sqlite://Resources/______.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


YelpData = Base.classes.yelpdata
Commercial = Base.classes.commercial
HTownDemo = Base.classes.htowndemo
session = Session(engine)
Base.metadata.create_all(engine)

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all routes that are available."""
    return (
        f"The Available Routes are:<br/>"
        f"/api/v1.0/Htown_Demographics<br/>"
        f"/api/v1.0/Commercial_Data<br/>"
        f"/api/v1.0/Yelp_Data<br/>"
    )

@app.route("/api/v1.0/Htown_Demographics")
def demographics():
    HtownStats = session.query(HTownDemo.htowndemo).all()
    return jsonify(HtownStats)

@app.route("/api/v1.0/Commercial_Data")
def commercial():
    Locations = session.query(Commercial.commercial).all()
    return jsonify(Locations)

@app.route("/api/v1.0/Yelp_Data")
def yelpdata():
    Restaurants = session.query(YelpData.yelpdata).all()
    return jsonify(Restaurants)


if __name__ == "__main__":
    app.run(debug=True)