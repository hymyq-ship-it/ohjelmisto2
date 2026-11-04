class koulu:
    def __init__(self, nimi, syntymävuosi, lasnaolo="on paikallaan" or "ei ole paikallaan"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.lasnaolo = lasnaolo

    def kerrat_lasnaolo(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " on " + self.lasnaolo)
        return

class luokka:
    def __init__(self):
        self.luokka = []

    def opiskelia_paikalla(self, opiskelia):
        self.opiskelia.append(opiskelia)
        print(opiskelia.nimi + " kirjattu sisään")
        return

    def opiskelia_eipaikalla(self, opiskelia):
        self.opiskelia.remove(opiskelia)
        print(opiskelia.nimi + " kirjattu ulos")
        return

    def tervehdi_opiskelijat(self):
        for opiskelia in self.opiskelia:
            opiskelia.kerrat_lasnaolo(1)

# Pääohjelma

kutsu1= koulu("huma", 2005, "on paikallaan")
kutsu2= koulu("Zainab", 2006, "ei ole paikallaan")

luokka = luokka()

luokka.opiskelia_paikalla(kutsu1)
luokka.opiskelia_paikalla(kutsu2)
luokka.tervehdi_opiskelijat()
