class Koira:
    tehty=0 #luokamuutuja, ja sanotaan property4

    def __init__(self, nimi, syntymävuosi, hauko="vuu_vuu"):
        self.nimi=nimi
        self.syntymävuosi=syntymävuosi
        self.hauko=hauko
        Koira.tehty+=1

    def hauku(self, kerrat):
        for _ in range(kerrat):
            print(self.hauko)
        