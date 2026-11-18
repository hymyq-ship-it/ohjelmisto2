from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Yhdistä tietokantaan - nämä ovat kurssin oletusarvot, tarkista omasi
def hae_yhteys():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        database="flight_game",
        user="root",
        password="",
        autocommit=True
    )

@app.route("/kenttä/<koodi>")
def hae_kentta(koodi):
    yhteys = hae_yhteys()
    kursori = yhteys.cursor(dictionary=True)
    
    # Haetaan vain se kenttä, jonka ICAO on sama kuin osoitteessa
    sql = "SELECT ident AS ICAO, name AS Name, municipality AS Municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (koodi,))
    tulos = kursori.fetchone()
    
    kursori.close()
    yhteys.close()
    
    if tulos:
        return jsonify(tulos)
    else:
        return jsonify({"virhe": "Kenttää ei löytynyt"}), 404

if __name__ == "__main__":
    app.run(port=3000)