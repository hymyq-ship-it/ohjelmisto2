from flask import Flask, jsonify
app=Flask(__name__) #luodaan keitiö



#lisän ruokalistalle kohta nimeltän /summa
@app.route("/summa")


# tehdän kone, että jos joku tila jotai 
#tee tämä
def summa():
    return jsonify({"tulos": 2+3 }) 
    #anna jsonifylle takaisin

if __name__ =="__main__":
    app.run()
