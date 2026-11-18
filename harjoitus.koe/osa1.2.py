class Olohuone:
    def __init__(self, sohva, matto):
        self.sohva=sohva
        self.matto=matto


class Home:

    def __init__(self, makkari, vessa):
        self.makkari=makkari
        self.vessa=vessa
        self.olohuone=Olohuone("divani", 2)



a=Home("sängy", "paperi")

print(a.olohuone.matto)