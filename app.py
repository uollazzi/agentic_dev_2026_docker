from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    now = datetime.now()

    with open("/usr/src/logs/log.txt", "a", encoding="utf-8") as f:
        f.write(now.strftime("%d/%m/%Y %H:%M"))

    # return f"<html><head></head><body><h1 style='color:red'>Sono le ore {now.strftime("%H:%M:%S")} del {now.strftime("%d/%m/%Y")}</h1></body></html>"
    return f"Sono le ore {now.strftime("%H:%M:%S")} del {now.strftime("%d/%m/%Y")}"


@app.route("/prodotti")
def prodotti():
    return ["mela", "pera"]
