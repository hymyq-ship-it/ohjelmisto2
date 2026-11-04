class Kaytaja:
    def __init__(self, kerros):
        self.kerros = kerros

class Rakennus:
    def __init__(self,kutsu, teksti="Olet kerroksessa "):
        self.kutsu = kutsu
        self.teksti = teksti

a= Kaytaja("x")
b= Rakennus(a)
print(b.teksti + str(b.kutsu.kerros))

