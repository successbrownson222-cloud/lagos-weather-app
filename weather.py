# Lagos Weather App - by Success Brownson (No requests needed)
import urllib.request
import json

city = "Lagos"

print("=== LAGOS WEATHER APP ===\n")
print(f"Checking weather for {city}...\n")

try:
    url = f"https://wttr.in/{city}?format=j1"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        current = data['current_condition'][0]
        temp = current['temp_C']
        desc = current['weatherDesc'][0]['value']
        humidity = current['humidity']
        wind = current['windspeedKmph']

        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {desc}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind} km/h")

except Exception as e:
    print(f"Error: {e}")
    print("Try again with data on")

print("\nPowered by wttr.in - Built by Success")