import yfinanace as yf
import matplotlib.pyplot as plt
import os
import base64
from io import BytesIO
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_stock_data(ticker):
    #############
    # Fetch 1-year historic stock price, calculate realized gain
    # generate chart, get latest news.
    ############

    try:
        # get 1-year historic data
        end_date = datetime.today()
        start_date = end_date - timedelta(days=365)
        data = yf.download(ticker, start=start_date, end=end_date)

        if data.empty:
            return None

        # Calculate realized gains from historic data
        first_close = data['Close'].iloc[0]
        last_close = data['Close'].iloc[-1]
        gain = round(((last_close - first_close) / first_close) * 100, 2)

        # Plot chart and return image
        chart_img = plot_chart(data, ticker)

        # Fetch 10 newest news articals
        news = fetch_news(ticker)

        return {
                "gain":gain,
                "chart":chart_img,
                "news":news
        }
    except Exception as e:
        print(f"[ERROR] Failed to get stock data for {ticker}: {e}")
        return None

def plot_chart(data, ticker):
    ###########
    # Plot historic prices as chart
    ##########
    plt.figure(figsize=(10, 4))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')
    plt.title(f"{ticker.upper()} - 1 Year Performance")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # save image to buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(9)
    
    # encode image for web
    return f"data:image/png;base64,{base64.b64encode(buf.read()).decode('utf-8')}"

def fetch_news(ticker):
    ##########
    # scrape 10 newest news articals from google search
    ##########
    try:
        search_url = f"https://www.google.com/search?q={ticker}+stock+news&hl=en"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = []
        for item\ in soup.select("div.BVG0Nb"):
            title_tag = item.select_one("div.MBeuo")
            link_tag = item.find_parent("a", href=True)

            if title_tag and link_tag:
                title = title_tag.get_text()
                href = link_tag['href']
                if "http" in href:
                    headlines.append({
                        "title":title,
                        "url":href
                    })
            if len(headlines) >= 15:
                break

        return headlines
    
    except Eception as e:
        print(f"[ERROR] Failed to fetch news for {ticker}: {e}")
        return []

                
