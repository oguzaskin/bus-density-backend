from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bus_data = {}

@app.route("/")
def home():
    return "API çalışıyor"

# 🔹 VERİ GÖNDERME (YENİ)
@app.route("/update/<int:bus_id>", methods=["POST"])
def update_bus(bus_id):
    data = request.json
    count = data.get("count", 0)
    bus_data[bus_id] = count
    return jsonify({"status": "ok", "bus_id": bus_id, "count": count})

# 🔹 VERİ ÇEKME
@app.route("/bus/<int:bus_id>")
def get_bus(bus_id):
    count = bus_data.get(bus_id, 0)
    return jsonify({"count": count})

if __name__ == "__main__":
    app.run()
