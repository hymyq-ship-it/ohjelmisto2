import requests
try:
    vastaus= requests.get("https://api.chucknorris.io/jokes/random")
    if vastaus.status_code==200:
        data = vastaus.json()
        print(data["value"])
    else:
        print("Haku epäonnistui")
except requests.exceptions.RequestException:
    print("Hakua ei voitu suorittaa.")
