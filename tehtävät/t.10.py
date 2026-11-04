import random  # tarvitaan nopeuden arpomiseen

class Auto:  # tämä on se vanha Auto-luokka edellisestä tehtävästä
    def __init__(self, rekisteritunnus, huippunopeus):  # alustaja
        self.rekisteritunnus = rekisteritunnus  # auton nimi/rekkari
        self.huippunopeus = huippunopeus  # maksimi nopeus, esim 150
        self.nopeus = 0  # tämän hetkinen nopeus, alussa 0
        self.matka = 0  # kuljettu matka, alussa 0

    def kiihdytä(self, muutos):  # muuttaa nopeutta
        self.nopeus += muutos  # lisää muutos nopeuteen
        if self.nopeus > self.huippunopeus:  # jos menee yli huipun
            self.nopeus = self.huippunopeus  # rajoita huippuun
        if self.nopeus < 0:  # jos menee alle 0
            self.nopeus = 0  # rajoita nollaan

    def kulje(self, tunti=1):  # ajaa tunnin eteenpäin
        self.matka += self.nopeus * tunti  # matka = nopeus * aika

class Kilpailu:  # UUSI LUOKKA - tämä on se mitä tehtävä pyytää
    def __init__(self, nimi, pituus, autot):  # alustaja saa nimen, pituuden ja autolistan
        self.nimi = nimi  # esim "Suuri romuralli"
        self.pituus = pituus  # esim 8000 km
        self.autot = autot  # lista autoista, TÄMÄ ON SE ASSOSIAATIO

    def tunti_kuluu(self):  # yksi tunti kuluu kisassa
        for auto in self.autot:  # käy jokainen auto läpi
            muutos = random.randint(-10, 15)  # arvo nopeuden muutos -10 ja 15 välillä
            auto.kiihdytä(muutos)  # muuta auton nopeutta
            auto.kulje(1)  # aja autolla yksi tunti

    def tulosta_tilanne(self):  # tulostaa taulukon
        print(f"\nKilpailu: {self.nimi} - Pituus: {self.pituus} km")
        print(f"{'Rekkari':<10} {'Huippu':<8} {'Nopeus':<8} {'Matka':<10}")
        print("-" * 40)
        for auto in self.autot:  # jokainen auto rivi kerrallaan
            print(f"{auto.rekisteritunnus:<10} {auto.huippunopeus:<8} {auto.nopeus:<8} {auto.matka:<10.1f}")

    def kilpailu_ohi(self):  # tarkistaa onko joku maalissa
        for auto in self.autot:  # käy autot läpi
            if auto.matka >= self.pituus:  # jos joku on ajanut tarpeeksi
                return True  # kisa on ohi
        return False  # muuten ei ole ohi

# PÄÄOHJELMA
autot = []  # tyhjä lista autoille
for i in range(10):  # luodaan 10 autoa kuten edellisessä tehtävässä
    huippu = random.randint(100, 200)  # arvotaan huippunopeus 100-200
    rekisteri = f"ABC-{i+1}"  # keksitään rekkari ABC-1, ABC-2...
    autot.append(Auto(rekisteri, huippu))  # lisätään auto listaan

kisa = Kilpailu("Suuri romuralli", 8000, autot)  # luodaan kisa

tunnit = 0  # laskuri tunneille
while not kisa.kilpailu_ohi():  # niin kauan kun kisa ei ole ohi
    kisa.tunti_kuluu()  # kuluu yksi tunti
    tunnit += 1  # lisätään tunti
    if tunnit % 10 == 0:  # joka 10. tunti
        kisa.tulosta_tilanne()  # tulostetaan tilanne

kisa.tulosta_tilanne()  # lopuksi tulostetaan vielä kerran kun kisa on ohi
print(f"\nKisa loppui! Kesto: {tunnit} tuntia")