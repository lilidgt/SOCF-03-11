from flask import Flask

APP = Flask(__name__)

@APP.route("/")
def index():
    return (
        "<h1>Projeto II – Sistemas Operacionais em Cloud</h1>"
        "<p>Aplicação Flask inicial.</p>"
    )

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000, debug=True)