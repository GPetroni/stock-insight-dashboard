# utils/graph.py
import matplotlib.pyplot as plt
import io
import base64

def generate_stock_chart(df, ticker):
    plt.figure(figsize=(10, 4))
    plt.plot(df['Date'], df['Close'], color='cyan', linewidth=2)
    plt.title(f'{ticker.upper()} - Closing Price (1 Year)', color='white')
    plt.xlabel('Date', color='white')
    plt.ylabel('Price (USD)', color='white')
    plt.xticks(color='white')
    plt.yticks(color='white')
    plt.grid(True, linestyle='--', alpha=0.5)

    plt.gca().set_facecolor('#1e1e1e')
    plt.gcf().patch.set_facecolor('#121212')

    # Save chart to a BytesIO stream
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png', dpi=150, bbox_inches='tight', transparent=True)
    buf.seek(0)
    chart_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()
    return chart_base64

