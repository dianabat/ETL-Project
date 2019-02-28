
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
engine = create_engine('sqlite:///Resources/______.sqlite')?check_same_thread=False
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)



session = Session(engine)
Base.metadata.create_all(engine)

app = Flask(__name__)

@app.route("/api/v1.0/")

@app.route("/")
def welcome():
    """List all routes that are available."""
    return (
        f"The Available Routes are:<br/>"
    )
