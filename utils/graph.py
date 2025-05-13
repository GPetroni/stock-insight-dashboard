# utils/graph.py

import yfinance as yf
import matplotlib.pyplot as plt
import os

def generate_stock_chart(ticker):
    data = yf.Ticker(ticker).history(period="1y")
    if data.empty:
        return None
    
    chart_path = f'static/charts/{ticker}_1y.png'
    os.makedirs(os.path.dirname(chart_path), exist_ok=True)

    plt.figure(figsize=(10, 4))
    plt.plot(data.index, data['Close'], label='Close Price', color='cyan')
    plt.title(f"{ticker.upper()} - 1 Year Price")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return chart_path

