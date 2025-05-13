import streamlit as st

st.set_page_config(page_title="Stock Insight Dashboard")

st.title("📊 Stock Insight Dashboard")

ticker = st.text_input("Enter a stock ticker symbol (e.g., AAPL, TSLA)")

if ticker:
    st.write(f"Showing data for: **{ticker.upper()}**")
    # Future: add chart + news fetch here
