# Backend API - by Success Brownson
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import urllib.request
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weather/{city}")
def get_weather(city: str):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        with urllib.request.urlopen(url) as res:
            data = json.loads(res.read().decode())
            cur = data['current_condition'][0]
            return {
                "city": city,
                "temp": cur['temp_C'],
                "desc": cur['weatherDesc'][0]['value'],
                "humidity": cur['humidity'],
                "wind": cur['windspeedKmph']
            }
    except:
        return {"error": "Could not fetch weather"}

@app.get("/")
def home():
    return {"message": "Lagos Weather API is running!"}