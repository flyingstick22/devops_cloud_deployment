import streamlit as st
import pandas as pd
import requests
import json
import os

def app():

    #colleting data from API's and place them in variables
    iss_location = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
    astronauts_in_iss = requests.get("http://api.open-notify.org/astros.json")
    location  = iss_location.json()
    data1 = astronauts_in_iss.json()
    latitude = float(location["latitude"])
    longitude = float(location["longitude"])
    speed = int(location["velocity"])
    altitude = int(location["altitude"])

    #map & metrics visualization
    st.title("Where is ISS? This App is deployed through Github Actions to Heroku")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Speed km/h", speed)
    col2.metric("Altitude in km", altitude)
    col3.metric("Latitude", round(latitude,3))
    col4.metric("Longitude", round(longitude,3))
    location_for_map = pd.DataFrame({
        'lat' : [latitude],
        'lon' : [longitude]
    })
    st.map(location_for_map, zoom=1)
    
if __name__ == "__main__":
    port=os.environ.get('PORT')
    app()
