from flask import Flask, request, jsonify
import requests as req

app = Flask(__name__)

API_TOKEN = "8275310361:TxxWM4jh"   # apna token
API_URL = "https://leakosintapi.com/"

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query")
    if not query:
        return jsonify({"error": "query parameter required"}), 400

    payload = {
        "token": API_TOKEN,
        "request": query,
        "limit": 100,
        "lang": "en",
        "type": "json"
    }

    try:
        res = req.post(API_URL, json=payload)
        res.raise_for_status()
        return jsonify(res.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)