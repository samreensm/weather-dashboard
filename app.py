import streamlit as st
import requests

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

st.title("🌤️ Weather Dashboard")
city = st.text_input("Enter a city name", "Hyderabad")

if city:
    data = get_weather(city)
    if data.get("cod") != 200:
        st.error("City not found")
    else:
        st.metric("Temperature (°C)", data["main"]["temp"])
        st.metric("Humidity (%)", data["main"]["humidity"])
        st.metric("Wind Speed (m/s)", data["wind"]["speed"])