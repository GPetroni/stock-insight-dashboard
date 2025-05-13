import os
from flask import Flask, render_template, request
from utils.stock_data import get_stock_data  # Adjusted to import from the utils directory

os.environ['FLASK_ENV'] = 'development'

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ticker = request.form['ticker']
        stock_data = get_stock_data(ticker)

        if stock_data is None:
            return render_template('index.html', error="Stock data not found. Please try again.")

        # Extract stock data for display
        chart_url = stock_data.get('chart', '')
        gain = stock_data.get('gain', '')
        news_articles = stock_data.get('news', [])

        return render_template('index.html', chart_url=chart_url, gain=gain, news_articles=news_articles)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


