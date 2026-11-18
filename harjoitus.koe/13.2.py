
#model 1 Miten otetaan lukuja vastaan?
from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route("/summa/<int:luoka1>/<int:luoka2>")
def summa(luku1, luku2):
    return jsonify({"tulos": luku1+ luku2})

if __name__=="__main__":
    app.run()
