import requests
import os

# Get the API key from the environment
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_stock_news(ticker):
    # Use NewsAPI to fetch stock-related news
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&language=en&pageSize=10&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code != 200:
        return []

    # Extract articles from the response
    articles = response.json().get("articles", [])
    return [
        {"title": article["title"], "url": article["url"]}
        for article in articles
        if article.get("title") and article.get("url")
    ]
import requests
import os

# Get the API key from the environment
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

def get_stock_news(ticker):
    # Use NewsAPI to fetch stock-related news
    url = f"https://newsapi.org/v2/everything?q={ticker}&sortBy=publishedAt&language=en&pageSize=10&apiKey={NEWS_API_KEY}"
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code != 200:
        return []

    # Extract articles from the response
    articles = response.json().get("articles", [])
    return [
        {"title": article["title"], "url": article["url"]}
        for article in articles
        if article.get("title") and article.get("url")
    ]

