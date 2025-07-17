from flask import Flask, request, jsonify
from eido_boot import EidoCore

app = Flask(__name__)
eido = EidoCore()

@app.route("/dream", methods=["POST"])
def dream():
    data = request.json
    topic = data.get("topic")
    lens = data.get("lens")
    result = eido.dream_about(topic, lens)
    return jsonify(result)

@app.route("/manifest", methods=["GET"])
def manifest():
    return jsonify(eido.manifest.export())

@app.route("/diagnostic", methods=["GET"])
def diagnostic():
    return jsonify(eido.run_diagnostic())
