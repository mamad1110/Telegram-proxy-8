from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_API = "https://api.telegram.org"

@app.route("/<path:path>", methods=["GET", "POST"])
def proxy(path):
    url = f"{TELEGRAM_API}/{path}"

    try:
        if request.method == "POST":
            r = requests.post(url, json=request.json)
        else:
            r = requests.get(url, params=request.args)

        return r.content, r.status_code, r.headers.items()

    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/")
def home():
    return "Telegram Proxy Active"
