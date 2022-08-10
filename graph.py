from datetime import date, timedelta
import yfinance as yf
import pandas as pd
import streamlit as st

symbol = "ITC.NS"
today = date.today()
td = timedelta(3652.5)
prev_10 = today - td

data = yf.download(symbol,prev_10,today)
chart_data = pd.DataFrame(data['Adj Close'])

st.line_chart(chart_data, width=2000, height=500, use_container_width=True)