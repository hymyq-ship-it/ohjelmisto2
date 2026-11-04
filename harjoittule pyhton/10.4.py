class Kerros:
    def __init__(self, kerros):
        self.kerros = kerros
class Rakennus:
    def __init__(self, hissi, portat):
        self.hissi = hissi
        self.portat = portat

a= Kerros(4)
b= Rakennus("portaat",a)
print(b.portat.kerros)
