from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os
import json

Base = declarative_base()
class AustinLocations(Base):
    __tablename__ = "locations2"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    rating = Column(Float)
    user_ratings_total = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    types1 = Column(String(255))
    types2 = Column(String(255))
    types3 = Column(String(255))
    types4 = Column(String(255))
    types5 = Column(String(255))
    types6 = Column(String(255))
    types7 = Column(String(255))
    latitude_region = Column(String(255))
    user_input = Column(Boolean)

app = Flask(__name__)

db = SQLAlchemy(app)


# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("CONN")
engine = create_engine("postgres://project-2:catalinawinemixer@35.225.106.22:5432/locations")
session = Session(bind=engine)


@app.route("/")
def index():
    locations_db = session.query(AustinLocations).filter().limit(5)
    return render_template("index.html", locations_db=locations_db)

@app.route("/user_input", methods=['POST','GET'])
def user_input():
        name = request.form.get('name')
        latitude_region = request.form.get('latitude_region')
        types1 = request.form.get('types1')
        rating = request.form.get('rating')
        user_ratings_total = 1
        latitude = 0
        longitude = 0
        types2 = "none"
        types3 = "none"
        types4 = "none"
        types5 = "none"
        types6 = "none"
        types7 = "none"
        new_location = AustinLocations(name=name, rating=rating, types1=types1, latitude=latitude, longitude=longitude, types2=types2, types3=types3, types4=types4, types5=types5, types6=types6, types7=types7, latitude_region=latitude_region, user_input=True)
        session.add(new_location)
        session.commit()
        
        return render_template("user_input.html", data=(name, latitude_region, types1, rating))


@app.route("/filtered_data/")
def filtered_data():
    loc_data = []

    north_data = session.query(AustinLocations).filter(AustinLocations.latitude_region == "North").filter(AustinLocations.rating >= 4.0).filter(AustinLocations.types1 == "restaurant").all()
    
    for record in north_data:
        location_dict={
            "name": record.name,
            "ratings": record.rating,
            "num_user_ratings": record.user_ratings_total,
            "location": record.latitude_region,
            "type": record.types1
        }
        loc_data.append(location_dict)

    return jsonify(loc_data)

@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html")

@app.route("/final_schedule")
def final_schedule():
    # data= []

    # query=session.query(AustinLocations).filter()

    # for record in query:
    #     dict={
    #         "id": record.id,
    #         "name ": record.name,
    #         "rating": record.rating,
    #         "user_ratings_total": record.user_ratings_total,
    #         "latitude": record.latitude,
    #         "longitude": record.longitude,
    #         "types1" : record.types1,
    #         "types2": record.types2,
    #         "types3": record.types3,
    #         "types4": record.types4,
    #         "types5": record.types5,
    #         "types6": record.types6,
    #         "types7": record.types7,
    #         "latitude_region": record.latitude_region,
    #         "user_input": record.user_input,
    #     }
    #     data.append(dict)

    # return jsonify(data)
    return render_template("final_schedule.html")

if __name__ == "__main__":
    app.run(debug=True)
