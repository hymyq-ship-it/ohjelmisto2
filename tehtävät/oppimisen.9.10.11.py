
#
class koira:
    #classin sisäisen määrittelyn asiat kutsutaan propertie
    age=10 # jokaisella koiralla on ikä, joka on 10, eli jokaisella classilla voi määrittää muuttujia, jotka ovat kaikilla saman classin olioilla samat


    #funktionit joka ovat classin sisällä määritellään metodiksi, ja metodin ensimmäinen parametri on aina ##self
    #  joka viittaa siihen olioon, jota metodia kutsutaan
    def walk(self, nimi,age, paino, rotu):
        print(nimi, age, paino, rotu) # jokaisella koiralla on walk metodi, joka tulostaa "I am walking"
tiedot= koira()

tiedot.walk("Matti", 5, 20,"suomenpystykorva")


