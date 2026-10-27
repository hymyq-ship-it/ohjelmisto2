class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        self.tamanhetkinen_nopeus += nopeuden_muutos

        if self.tamanhetkinen_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus

        if self.tamanhetkinen_nopeus < 0:
            self.tamanhetkinen_nopeus = 0

    def kulje(self, aikaa):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * aikaa


auto = Auto("ABC-123", 142)

print("Rekisteritunnus:", auto.rekisteritunnus)
print("Huippunopeus:", auto.huippunopeus)
print("Nykyinen nopeus:", auto.tamanhetkinen_nopeus)
print("Kuljettu matka:", auto.kuljettu_matka)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)

print("Nopeus kiihdytysten jälkeen:", auto.tamanhetkinen_nopeus)

auto.kulje(1.5)

print("Kuljettu matka:", auto.kuljettu_matka)

auto.kiihdyta(-200)

print("Nopeus hätäjarrutuksen jälkeen:", auto.tamanhetkinen_nopeus)