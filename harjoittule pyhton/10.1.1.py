class gorbe:
    def __init__(self, nimi):
        self.nimi=nimi

class adam:
    def __init__(self, nimi):
        self.nimi=nimi
        self.gorbe=None

huma = adam("huma")
ninni=gorbe("ninni")

huma.gorbe=ninni #tällä class yhdistivat toisen kanssa

print(huma.nimi)
print(huma.gorbe.nimi)
