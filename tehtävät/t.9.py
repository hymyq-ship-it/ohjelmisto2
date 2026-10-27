from random import randint

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


# Luodaan 10 autoa
autot = []

for i in range(1, 11):
    rekisteri = f"ABC-{i}"
    huippunopeus = randint(100, 200)
    auto = Auto(rekisteri, huippunopeus)
    autot.append(auto)

# Kilpailu alkaa
kilpailu_paattynyt = False

while not kilpailu_paattynyt:

    for auto in autot:
        muutos = randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_paattynyt = True

# Tulostetaan tulokset taulukkona
print(f"{'Rekisteri':<12}{'Huippu':<10}{'Nopeus':<10}{'Matka':<12}")
print("-" * 44)

for auto in autot:
    print(
        f"{auto.rekisteritunnus:<12}"
        f"{auto.huippunopeus:<10}"
        f"{auto.nopeus:<10}"
        f"{auto.kuljettu_matka:.1f}"
    )