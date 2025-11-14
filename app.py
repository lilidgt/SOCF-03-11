from flask import Flask, jsonify

APP = Flask(__name__)

ESTUDANTES = "Lissa Deguti, Melissa Weiss e Fernanda Moraes"

@APP.route("/")
def index():
    return (
        "<h1>Projeto II – Sistemas Operacionais em Cloud</h1>"
        f"<p>Estudantes: {ESTUDANTES}</p>"
    )

@APP.route("/info")
def info():
    return jsonify({"estudantes": ESTUDANTES})

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000, debug=True)