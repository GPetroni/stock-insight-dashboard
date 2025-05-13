import yfinance as yf
import matplotlib.pyplot as plt
import os
import base64
from io import BytesIO
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_stock_data(ticker):
    # Fetch stock data using yfinance
    try:
        stock = yf.Ticker(ticker)
        stock_info = stock.history(period="1y")

        # Check if no stock data is returned
        if stock_info.empty:
            print(f"No stock data returned for {ticker}")
            return None

        # Calculate 1-year gain
        start_price = stock_info.iloc[0]['Close']
        end_price = stock_info.iloc[-1]['Close']
        one_year_gain = ((end_price - start_price) / start_price) * 100

        print(f"Stock Data: {stock_info}")

        # Example of generating a stock chart URL (replace with actual chart API implementation)
        chart_url = f'https://somechartapi.com/{ticker}.png'

        # Fetch stock news (Example: using BeautifulSoup)
        news_url = f"https://www.google.com/search?q={ticker}+stock+news"
        response = requests.get(news_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        news_articles = []
        for item in soup.find_all("div", {"class": "BVG0Nb"}):
            title = item.get_text()
            link = item.find('a')['href']
            news_articles.append({'title': title, 'url': f"https://www.google.com{link}"})

        # Return a dictionary with chart URL, gain percentage, and news articles
        return {
            'chart': chart_url,
            'gain': one_year_gain,
            'start_price': start_price,  # Include start_price
            'end_price': end_price,      # Include end_price
            'news': news_articles,
            'stock_data': stock_info  # Return the stock data as well
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
        for item in soup.select("div.BVG0Nb"):
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

                
