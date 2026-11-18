class Aiti:
    def __init__(self, nimi):
        self.nimi=nimi


class Lapsi(Aiti):
    def __init__(self,nimi,ikä):
        self.ikä=ikä
        super().__init__(nimi)

a=Lapsi("ninni", 2)
print(a.nimi)
print(a.ikä)
