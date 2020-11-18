import requests
import pandas as pd

df =pd.read_csv("project1/Data/mrgdata.csv")
df.head()

lat = []
lng = []
locations = []

keywords=[
    "tourist attraction",
    "shopping",
    "point of interest",
    "restaurant",
    "landmark",
    "establishment",
    "museum"
]

for x in df["Lat_bp"]:
    lat.append(x)
for y in df["Lng_bp"]:
    lng.append(y)

lat_lng_str = []
lat_lng = zip(lat, lng)
list(lat_lng)[0][0]

    
for index, row in df.iterrows():
    lat = row["Lat_bp"]
    lng = row["Lng_bp"]
    lat_lng_str.append(f"{lat}, {lng}")

lat_lng_str

for x in lat_lng_str: 
    for y in keywords:
        try:
            r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?", params={
            "location": x,
            "radius": 1000,
            "keyword": y,
            "key": "AIzaSyDb9PBr8sr8rbn1SsgATRHH513ptYPaxCc"
            })
            locations.append({
                "name": r.json()["results"][0]["name"],
                "rating": r.json()["results"][0]["rating"],
                "location": r.json()["results"][0]["geometry"]["location"],
                "user_ratings_total": r.json()["results"][0]["user_ratings_total"],
                "types": r.json()["results"][0]["types"]
            })
                
        except:
            locations.append(0)
            
for i in locations:
    if type(i) == int:
        locations.remove(i)
        
df = pd.DataFrame(locations)

df.to_csv("locations.csv")