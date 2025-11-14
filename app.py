from flask import Flask, jsonify
import os
import platform
import psutil

APP = Flask(__name__)

ESTUDANTES = "Lissa Deguti, Melissa Weiss e Fernanda Moraes"

def pegar_metricas():
    processo = psutil.Process(os.getpid())
    return {
        "pid": processo.pid,
        "memoria_usada": round(processo.memory_info().rss / (1024 * 1024), 2),
        "cpu_porcentagem": processo.cpu_percent(interval=0.1),
        "sistema_operacional": f"{platform.system()} ({platform.release()})",
        "estudantes": ESTUDANTES
    }

@APP.route("/")
def index():
    metrica = pegar_metricas()
    return (
        f"<h1>Projeto II – Sistemas Operacionais em Cloud</h1>"
        f"<p>Estudantes: {metrica['estudantes']}</p>"
        f"<p>PID: {metrica['pid']}</p>"
        f"<p>Memória usada: {metrica['memoria_usada']} MB</p>"
        f"<p>CPU: {metrica['cpu_porcentagem']}%</p>"
        f"<p>Sistema operacional: {metrica['sistema_operacional']}</p>"
    )

@APP.route("/info")
def info():
    return jsonify({"estudantes": ESTUDANTES})

@APP.route("/metricas")
def metricas():
    return jsonify(pegar_metricas())

if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000, debug=True)