from flask import Flask, request, jsonify
import subprocess
from urllib.parse import unquote

app = Flask(__name__)

@app.route("/marina", methods=["GET"])
def solve():

    laza= request.args.get("laza", "")

    if not laza:
        return jsonify({"error": "Paramètre 'laza' manquant"}), 400

    try:

        result = subprocess.run(
            ["./marina", laza], 
            capture_output=True,
            text=True,
            timeout=5
        )
        
        return jsonify({
            "stdout": result.stdout.strip(),
        })
    except subprocess.TimeoutExpired:
        return jsonify({"error": "Timeout"}), 500
    except Exception as e:
        return jsonify({"error": f"Erreur interne : {str(e)}"}), 500
    
@app.route("/ping")
def sayPong():
    return "pong", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
