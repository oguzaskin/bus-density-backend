from flask import Flask, jsonify, request
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

bus_data = {}
last_update = {}

# -------------------------
# ANA SAYFA
# -------------------------
@app.route("/")
def home():
    return "API çalışıyor!"

# -------------------------
# VERİ GÖNDERME
# -------------------------
@app.route("/update/<int:bus_id>", methods=["POST"])
def update_bus(bus_id):
    data = request.json
    count = data.get("count", 0)

    bus_data[bus_id] = count
    last_update[bus_id] = time.time()  # 🔥 kritik

    return jsonify({
        "status": "ok",
        "bus_id": bus_id,
        "count": count
    })

# -------------------------
# VERİ ÇEKME
# -------------------------
@app.route("/bus/<int:bus_id>")
def get_bus(bus_id):

    # 🔥 hiç veri yoksa
    if bus_id not in last_update:
        return jsonify({"count": 0})

    # 10sn sonra sıfırlama
    if time.time() - last_update[bus_id] > 10:
        return jsonify({"count": 0})

    return jsonify({
        "count": bus_data.get(bus_id, 0)
    })

# -------------------------
# DEBUG (opsiyonel)
# -------------------------
@app.route("/debug")
def debug():
    return jsonify({
        "bus_data": bus_data,
        "last_update": last_update
    })

# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
