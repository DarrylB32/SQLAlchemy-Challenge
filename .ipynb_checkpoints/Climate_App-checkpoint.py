import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement=Base.classes.measurement
Station=Base.classes.station

#################################################
# Flask Setup
#################################################

Climate_App = Flask(__name__)

#################################################
# Flask Routes
#################################################


app_index = {"Precipitation": "/api/v1.0/precipitation",
            "Stations":"/api/v1.0/stations",
            "Temperature Observervations":"/api/v1.0/tobs",
            "Temperature Min, Max, and Average (Specific Date)":"/api/v1.0/<start>",
            "Temperature Min. Max, and Average (Range of Dates)":"/api/v1.0/<start>/<end>"}


@Climate_App.route("/")
def home():
    print("Below is a list of the available routes:")
    return jsonify(app_index)


@Climate_App.route("/api/v1.0/precipitation")
def precipitation():
        # Create our session (link) from Python to the DB
    session = Session(engine)


    # Query all precipitation data
    results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation
    date_prcp = []
    for date, prcp in results:
        date_prcp_dict = {}
        date_prcp_dict[date] = prcp
        date_prcp.append(date_prcp_dict)

    return jsonify(date_prcp)


@Climate_App.route("/api/v1.0/stations")
def stations():
    session = Session(engine)


    # Query all precipitation data
    results = session.query(Station.station, Station.name).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation
    stations = []
    for station, name in results:
        station_dict = {}
        station_dict[station] = name
        stations.append(station_dict)

    return jsonify(stations)

@Climate_App.route("/api/v1.0/tobs")
def tobs1s():
    session = Session(engine)


    # Query all precipitation data
    results = session.query(Measurement.station, Measurement.tobs).filter((Measurement.station=="USC00519281"),(Measurement.date>='2016-08-23')).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation
    station_temp = []
    for station, tobs in results:
        station_temp_dict = {}
        station_temp_dict[station]=tobs
        station_temp.append(station_temp_dict)

    return jsonify(station_temp)

@Climate_App.route("/api/v1.0/<start>")
def start_date(start):
    session = Session(engine)


    # Query all precipitation data
    results = session.query(Measurement.date, func.max(Measurement.tobs), func.avg(Measurement.tobs), func.min(Measurement.tobs)).filter(Measurement.date>= start).group_by(Measurement.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation
    start_temp = []
    for date, maximum, average, minimum in results:
        start_temp_dict = {}
        start_temp_dict['1-TDATE'] =date
        start_temp_dict['2-TMAX'] =maximum
        start_temp_dict['3-TAVG'] =average
        start_temp_dict['4-TMIN'] =minimum
        
        start_temp.append(start_temp_dict)

    return jsonify(start_temp)

@Climate_App.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    session = Session(engine)


    # Query all precipitation data
    results = session.query(Measurement.date, func.max(Measurement.tobs), func.avg(Measurement.tobs), func.min(Measurement.tobs)).filter((Measurement.date>= start), (Measurement.date<=end)).group_by(Measurement.date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of precipitation
    start_end_temp = []
    for date, maximum, average, minimum in results:
        start_end_temp_dict = {}
        start_end_temp_dict['1-TDATE'] =date
        start_end_temp_dict['2-TMAX'] =maximum
        start_end_temp_dict['3-TAVG'] =average
        start_end_temp_dict['4-TMIN'] =minimum
        
        start_end_temp.append(start_end_temp_dict)

    return jsonify(start_end_temp)

if __name__ == "__main__":
    Climate_App.run(debug=True)
