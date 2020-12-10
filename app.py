from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os

Base = declarative_base()
class AustinLocations(Base):
    __tablename__ = "locations2"

    id = Column(Integer, primary_key=True)
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

times = [
    "9:00 AM",
    "11:00 AM",
    "1:00 PM",
    "3:00 PM",
    "5:00 PM",
    "7:00 PM"
]

app = Flask(__name__)

db = SQLAlchemy(app)

# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("CONN")
engine = create_engine("postgres://project-2:catalinawinemixer@35.225.106.22:5432/locations")
session = Session(bind=engine)



@app.route("/")
def index():
    locations_db = session.query(AustinLocations).filter().limit(5)
    return render_template("index.html", locations_db=locations_db)

@app.route("/user_input")
def user_input():
    return render_template("user_input.html")

@app.route("/filtered_data", methods = ['POST', 'GET'])
def filtered_data():
    if request.method == 'GET':
        return f"The URL /filtered_data is accessed directly. Try going to /user_input to submit form"
    if request.method == 'POST':
        user_input_data = request.user_input
        return render_template("filtered_data.html", user_input_data = user_input_data)

@app.route("/visualizations")
def visualizations():
    return "hi"

@app.route("/final_schedule")
def final_schedule():
    locations_db = session.query(AustinLocations).filter().all()
    return render_template("final_schedule.html", times=times)

if __name__ == "__main__":
    app.run(debug=True)
