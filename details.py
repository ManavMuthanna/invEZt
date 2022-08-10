symbol = "INFY.NS"

from yahooquery import Ticker
import pandas as pd
import streamlit as st

stock1 = Ticker(symbol)
Modules = stock1.all_modules
Quotes = stock1.quotes
Fin_Data = stock1.financial_data
Sum_Data = stock1.summary_detail

df = pd.DataFrame(columns = ['Market Cap', 'EPS'])

cur = Quotes[symbol]['currency']
#st.header("Market Currency:")
#st.subheader(cur)
#st.caption("All metrics will be in this currency")

name = Quotes[symbol]['longName']

sector = Modules[symbol]['assetProfile']['sector']


market_cap = (Sum_Data[symbol]['marketCap'])
market_cap = round(market_cap)

eps = Quotes[symbol]['epsTrailingTwelveMonths']
eps = round(eps,2)

roe = Fin_Data[symbol]['returnOnEquity']*100
roe = round(roe,2)


pe = Quotes[symbol]['trailingPE']
pe = round(pe,2)


dte = Fin_Data[symbol]['debtToEquity']
dte = round(dte,2)


pb = Quotes[symbol]['priceToBook']
pb = round(pb,2)


ps = Sum_Data[symbol]['priceToSalesTrailing12Months']
ps = round(ps,2)

peg = Modules[symbol]['indexTrend']['pegRatio']
peg = round(peg,2)
 

cr = Fin_Data[symbol]['currentRatio']
cr = round(cr,2)


try:
    dy = Sum_Data[symbol]['dividendYield']*100
    dy = round(dy,2)
except KeyError:
    dy = Sum_Data[symbol]['dividendYield'] = "n/A"

insiders = Modules[symbol]['defaultKeyStatistics']['heldPercentInsiders']*100
insiders = round(insiders,2)

print(Quotes)