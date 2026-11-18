class Moottori:    #ruoka



    #ruokan ohje
    def __init__(self, teho, tyyppi):    
        self.teho = teho
        self.tyyppi = tyyppi




class Auto:   #ruoka


    #ruoka ohje
    def __init__(self, merkki, malli, vuosi):
        self.merkki = merkki
        self.malli = malli
        self.vuosi = vuosi
        self.moottori = Moottori(150, "bensa")  # Auto OMISTAA Moottorin

    def kaynnista(self):
        print(f"{self.moottori.tyyppi} moottori käynnistyy")



auto= Auto("Toyota", "Corolla", 2020)
print(auto.moottori.tyyppi)  # bensa