from flask import Flask, request
app = Flask(__name__)

@app.toute("/henkilot", methods=["GET"])
#sanoin ohjelmalle että minne meenet hakemaan tietoa ja
#  minkän methodilla pääset

#nyt tehdän metodi(funktion)
def hae():
    args= request.args
    luku1=float(args("luku1"))


    