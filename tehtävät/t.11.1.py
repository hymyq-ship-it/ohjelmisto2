class Julkaisu:  # YLILUOKKA, vanhempi kaikille
    def __init__(self, nimi):  # jokaisella julkaisulla on nimi
        self.nimi = nimi  # tallennetaan nimi

class Kirja(Julkaisu):  # ALILUOKKA, perii Julkaisun
    def __init__(self, nimi, kirjoittaja, sivumaara):  # saa 3 tietoa
        super().__init__(nimi)  # kutsutaan vanhempaa, se hoitaa nimen
        self.kirjoittaja = kirjoittaja  # oma tieto
        self.sivumaara = sivumaara  # oma tieto

    def tulosta_tiedot(self):  # oma metodi
        print(f"Kirja: {self.nimi}, kirjoittaja {self.kirjoittaja}, {self.sivumaara} sivua")

class Lehti(Julkaisu):  # TOINEN ALILUOKKA
    def __init__(self, nimi, paatoimittaja):  # saa 2 tietoa
        super().__init__(nimi)  # vanhempi hoitaa nimen
        self.paatoimittaja = paatoimittaja  # oma tieto

    def tulosta_tiedot(self):  # oma metodi
        print(f"Lehti: {self.nimi}, päätoimittaja {self.paatoimittaja}")

# PÄÄOHJELMA 1
aku = Lehti("Aku Ankka", "Aki Hyyppä")  # luodaan lehti
hytti = Kirja("Hytti n:o 6", "Rosa Liksom", 200)  # luodaan kirja

aku.tulosta_tiedot()  # tulostetaan
hytti.tulosta_tiedot()