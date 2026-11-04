from flask import Flask, jsonify , request
from hesap import topla, cikar, carp, bol

app = Flask(__name__)

@app.get("/health")
def health_check():
    return jsonify({"status": "ok"})  

def _sayilari_al():
    try:
        return float(request.args["a"]), float(request.args["b"])
    except (KeyError, ValueError):
        return None


def _islem(fonksiyon):
    sayilar = _sayilari_al()
    if sayilar is None:
        return jsonify(hata="a ve b sayi olmali"), 400
    try:
        return jsonify(sonuc=fonksiyon(*sayilar))
    except ValueError as hata:
        return jsonify(hata=str(hata)), 400


@app.get("/topla")
def topla_endpoint():
    return _islem(topla)


@app.get("/cikar")
def cikar_endpoint():
    return _islem(cikar)


@app.get("/carp")
def carp_endpoint():
    return _islem(carp)


@app.get("/bol")
def bol_endpoint():
    return _islem(bol)