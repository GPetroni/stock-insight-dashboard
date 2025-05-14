import os
import io
import base64
import requests
from PIL import Image
from flask import Flask, render_template, request
from utils.stock_data import get_stock_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    stock_data = None
    ticker = None

    if request.method == "POST":
        ticker = request.form.get("ticker")
        if ticker:
            stock_data = get_stock_data(ticker)

    return render_template("index.html", stock_data=stock_data, ticker=ticker)

if __name__ == "__main__":
    # Ensures that changes to CSS/HTML/JS are not cached during development
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    # Run the server on all IPs (accessible on LAN) and enable debug mode
    app.run(host="0.0.0.0", port=5000, debug=True)

