import requests

paikka = input("Anna paikkakunta: ")
avain = "653df648365a781a1ed87f50aebaf3f8"

pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikka}&appid={avain}&units=metric&lang=fi"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        data = vastaus.json()
        print(data["weather"][0]["description"])
        print(data["main"]["temp"], "°C")
    else:
        print("Paikkakuntaa ei löytynyt")
except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa.")