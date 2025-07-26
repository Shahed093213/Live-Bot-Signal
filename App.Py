from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# ডেমো র্যান্ডম সিগনাল তৈরি
def generate_signal(asset):
    directions = ['Buy', 'Sell']
    signal = {
        "asset": asset,
        "direction": random.choice(directions),
        "confidence": f"{random.randint(75, 95)}%"
    }
    return signal

@app.route('/signal', methods=['GET'])
def signal():
    asset = request.args.get('asset')
    if not asset:
        return jsonify({"error": "Missing asset parameter"}), 400
    result = generate_signal(asset)
    return jsonify(result)

@app.route('/')
def home():
    return 'Quotex Signal API is Running ✅'

if __name__ == '__main__':
    app.run(debug=True)