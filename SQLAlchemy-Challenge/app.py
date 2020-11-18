import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def welcome():
    return(
        f"Welcome to the Climate App API!<br/>"
        f"Available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)

    final_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(weeks=52)

    date_precip = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_ago, Measurement.date <= '2017-08-23').\
        order_by(Measurement.date).all()

    session.close()

    precip_values = []
    for date, prcp in date_precip:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip_values.append(precip_dict)

    return jsonify(precip_values)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)

    station_list = session.query(Station.station).all()

    session.close()

    all_stations = list(np.ravel(station_list))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)

    active_final_date = session.query(Measurement.date).filter(Measurement.station == 'USC00519281').\
                    order_by(Measurement.date.desc()).first()

    active_year_ago = dt.date(2017, 8, 18) - dt.timedelta(weeks=52)

    most_active_station = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281', Measurement.date >= active_year_ago, Measurement.date <= '2017-08-18').all()

    session.close()

    most_active_tobs = list(np.ravel(most_active_station))
    
    return jsonify(most_active_tobs)

@app.route("/api/v1.0/<start>")
def start_temp(start):
    session = Session(engine)

    start_temps = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    start_values = session.query(*start_temps).filter(Measurement.date >= start).all()

    session.close()

    return jsonify(start_values)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    session = Session(engine)

    start_end_temps = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    start_end_values = session.query(*start_end_temps).filter(Measurement.date >= start, Measurement.date <= end).all()

    session.close()

    return jsonify(start_end_values)

if __name__ == '__main__':
    app.run(debug=True)
