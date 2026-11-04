import requests 

nimi = input("Anna pokemonin nimi: ").lower().strip()  # esim pikachu tai salamence

# 1. tehdään pyyntö (request) palvelimelle
vastaus = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nimi}")

# 2. tarkistetaan statuskoodi
if vastaus.status_code == 200:  # 200 = OK
    data = vastaus.json()  # muutetaan JSON -> Python dict
    
    # 3. otetaan tyypit, pokemoneilla voi olla 1 tai 2 tyyppiä
    tyypit = []
    for t in data["types"]:
        tyypit.append(t["type"]["name"])
    
    print(f"{nimi} tyyppi on: {', '.join(tyypit)}")
    
else:  # jos statuskoodi on 404 Not Found
    print("Pokemonia ei löytynyt, tarkista nimi")