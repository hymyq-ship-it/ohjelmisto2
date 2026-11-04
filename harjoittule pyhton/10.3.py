class nimi:
    def __init__(self, huma):
        self.huma =huma


class Auto:
    def __init__(self, merkki, vuosi, motori):
        self.merkki = merkki
        self.vuosi=vuosi
        self.motori = motori

m= nimi(200)
a= Auto("toyota",m, 2020)
print(a.merkki, a.vuosi)
print(a.vuosi.huma) 


