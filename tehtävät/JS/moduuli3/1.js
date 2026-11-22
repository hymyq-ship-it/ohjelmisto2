pituus = int(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Laske kuha takaisin järveen! Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} cm.")
else:
    print("Kuha on mitallinen.")