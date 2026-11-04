class Auto:  # vanha Auto-luokka, yliluokka
    def __init__(self, rekkari, huippu):  # rekisteri ja huippunopeus
        self.rekkari = rekkari
        self.huippu = huippu
        self.nopeus = 0  # alussa 0
        self.matka = 0  # alussa 0

    def kiihdyta(self, muutos):  # muuttaa nopeutta
        self.nopeus += muutos
        if self.nopeus > self.huippu:  # ei yli huipun
            self.nopeus = self.huippu
        if self.nopeus < 0:  # ei alle 0
            self.nopeus = 0

    def kulje(self, tunti):  # ajaa
        self.matka += self.nopeus * tunti  # matka = nopeus * aika

class Sahkoauto(Auto):  # perii Auton
    def __init__(self, rekkari, huippu, akku):  # saa 3 tietoa
        super().__init__(rekkari, huippu)  # vanhempi hoitaa 2 ekaa
        self.akkukapasiteetti = akku  # oma, kWh

class Polttomoottoriauto(Auto):  # toinen lapsi
    def __init__(self, rekkari, huippu, tankki):  # saa 3 tietoa
        super().__init__(rekkari, huippu)  # vanhempi hoitaa 2 ekaa
        self.tankki = tankki  # oma, litraa

# PÄÄOHJELMA 2
sahko = Sahkoauto("ABC-15", 180, 52.5)  # luodaan sähköauto
poltto = Polttomoottoriauto("ACD-123", 165, 32.3)  # luodaan polttis

sahko.kiihdyta(100)  # asetetaan nopeus 100
poltto.kiihdyta(80)  # asetetaan nopeus 80

sahko.kulje(3)  # ajetaan 3 tuntia
poltto.kulje(3)

print(f"Sähköauto {sahko.rekkari} ajoi {sahko.matka} km")  # 300 km
print(f"Polttis {poltto.rekkari} ajoi {poltto.matka} km")  # 240 km