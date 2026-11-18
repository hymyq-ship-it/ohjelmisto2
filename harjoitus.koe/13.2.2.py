#Tapa B: Kysymysmerkin jälkeen (kyselyparametri)
from flask import Flask , jsonify, request
app=Flask(__name__)
@app.route("/summa")
def summa():
    luku1 = int(request.args.get("luku1"))
    luku2 = int(request.args.get("luku2"))
    return jsonify({"tulos": luku1 + luku2})