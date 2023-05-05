import yfinance as yf
import streamlit as st

st.set_page_config(layout="wide")
st.title("invEZt")

symbol = ""
symbol = st.text_input("Enter A Stock Symbol")
stock = yf.Ticker(symbol)

st.write("If you are trying to get the data for stocks of a market other than the US, add the market symbol after the ticker symbol\nFor example: The Indian Company Infosys would be 'INFY.NS'")

disclaimer = st.empty()
disclaimer.text("Disclaimer!\nDo not use only the data from this app to invest your money.\nAll decisions in stock market investing must be done after careful evaluation of many factors. \nThis is simply an analysis tool.")

if(symbol != ""):
    disclaimer.empty()
    from yahooquery import Ticker
    stock1 = Ticker(symbol)
    Modules = stock1.all_modules
    Quotes = stock1.quotes
    Fin_Data = stock1.financial_data
    Sum_Data = stock1.summary_detail

    cur = Quotes[symbol]['currency']

    name = Quotes[symbol]['longName']
                     
    sector = Modules[symbol]['assetProfile']['sector']
    
    pc = Quotes[symbol]['regularMarketPreviousClose']

    market_cap = (Sum_Data[symbol]['marketCap'])/1000000000
    market_cap = round(market_cap,2)
    
    try:
        eps = Quotes[symbol]['epsTrailingTwelveMonths']
        eps = round(eps,2)
    except KeyError:
        eps = Quotes[symbol]['epsTrailingTwelveMonths'] = "N/A"
     
    try:
        roe = Fin_Data[symbol]['returnOnEquity']*100
        roe = round(roe,2)
    except KeyError:
        roe = Fin_Data[symbol]['returnOnEquity'] = "N/A"

    try:
        pe = Quotes[symbol]['trailingPE']
        pe = round(pe,2)
    except KeyError:
        pe = Quotes[symbol]['trailingPE'] = "N/A"

    try:
        dte = Fin_Data[symbol]['debtToEquity']
        dte = round(dte,2)
    except KeyError:
        dte = Fin_Data[symbol]['debtToEquity'] = "N/A"

    try:
        pb = Quotes[symbol]['priceToBook']
        pb = round(pb,2)
    except KeyError:
        pb = Quotes[symbol]['priceToBook'] = "N/A" 

    try:
        ps = Sum_Data[symbol]['priceToSalesTrailing12Months']
        ps = round(ps,2)
    except KeyError:
        ps = Sum_Data[symbol]['priceToSalesTrailing12Months'] = "N/A"

    try:    
        peg = Modules[symbol]['indexTrend']['pegRatio']
        peg = round(peg,2) 
    except KeyError:
        peg = Modules[symbol]['indexTrend']['pegRatio'] = "N/A"

    try:
        cr = Fin_Data[symbol]['currentRatio']
        cr = round(cr,2)
    except KeyError:
        cr = Fin_Data[symbol]['currentRatio'] = "N/A"
        
    try:
        dy = Sum_Data[symbol]['dividendYield']*100
        dy = round(dy,2)
    except KeyError:
        dy = Sum_Data[symbol]['dividendYield'] = "N/A"
    
    insiders = Modules[symbol]['defaultKeyStatistics']['heldPercentInsiders']*100
    insiders = round(insiders,2)


    info = stock1.asset_profile

    bs = stock1.balance_sheet()

    cf = stock1.cash_flow(trailing=False)

    fin = stock1.all_financial_data()

    ni = cf["NetIncome"][0]

    def roa():
        c_tca = bs["TotalAssets"][0]
        c_tl = bs["TotalLiabilitiesNetMinorityInterest"][0]
        c_roa = c_tca/c_tl
        return c_roa

    def ocf():
        try:
            c_ocf = int(cf["OperatingCashFlow"][0])
            return c_ocf
        except KeyError:
            c_ocf = 0
            return c_ocf
        
    def current_ratio():
        c_tca = fin["CurrentAssets"][0]
        py_tca = fin["CurrentAssets"][1]
        c_tl = bs["CurrentLiabilities"][0]
        py_tl = bs["CurrentLiabilities"][1]
        r1 = c_tca/c_tl
        r2 = py_tca/py_tl
        if r1 > r2:
            return 1
        else:
            return 0

    def gross_margin():
        c_gm = fin["GrossProfit"][0]
        py_gm = fin["GrossProfit"][1]
        return c_gm - py_gm

    def at_ratio():
        c_assets = fin["TotalAssets"][0]
        py1_assets = fin["TotalAssets"][1]
        py2_assets = fin["TotalAssets"][2]
        av1 = (c_assets+py1_assets)/2
        av2 = (py1_assets+py2_assets)/2
        atr1 = fin["TotalRevenue"][0]/av1
        atr2 = fin["TotalRevenue"][1]/av2
        return atr1-atr2

    def new_shares():
        c_ns = fin['CommonStock'][0]
        py_ns = bs['CommonStock'][1]
        if c_ns - py_ns == 0:
            return 1
        else:
            return 0

    def lt_debt():
        try:
            c_lt_debt = bs["NonCurrentDeferredLiabilities"][0]
        except KeyError:
            c_lt_debt = 0
        try:
            py_lt_debt = bs["NonCurrentDeferredLiabilities"][1]
        except KeyError:
            py_lt_debt = 0

        if c_lt_debt < py_lt_debt:
            return 1
        else:
            return 0
            
    def get_piotroski_score():
        score = 0

        if ni > 0:
            score = score + 1
            print("ni",score)

        if roa() > 0:
            score = score + 1
            print("roa",score)

        if ocf() > 0:
            score = score + 1
            print("ocf",score)

        if ocf() > ni:
            score = score + 1
            print("ocf > ni",score)

        if lt_debt() > 0:
            score = score + 1
            print("ltd",score)

        if current_ratio() > 0:
            score = score + 1
            print("cr",score)

        if new_shares() > 0:
            score = score + 1
            print("ns",score)

        if gross_margin() > 0:
            score = score + 1
            print("gm",score)
        
        if at_ratio() > 0:
            score = score + 1
            print("atr",score)
        
        return score

    roa()
    ocf()
    lt_debt()
    current_ratio()
    new_shares()
    gross_margin()
    at_ratio()

    p_score = get_piotroski_score()

    cola,colb = st.columns(2)

    with cola:
         st.subheader("Market Currency:")
    
    with colb:
        st.subheader(cur)

    st.caption("All metrics will be in this currency")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Company Name:")
        st.subheader("Sector:")
        st.subheader("Previous Close:")
        st.subheader("Market Cap (in Billions):")
        st.subheader("EPS:")
        st.subheader("RoE in %:")
        st.subheader("P/E Ratio:")
        st.subheader("Debt/Equity Ratio:")
        st.subheader("P/B Ratio:")
        st.subheader("P/S Ratio:")
        st.subheader("PEG Ratio:")
        st.subheader("Current Ratio:")
        st.subheader("Dividend Yield%:")
        st.subheader("% Of Insider stake:")

    with col2:
        st.subheader(name) 
        st.subheader(sector)
        st.subheader(pc)
        st.subheader(market_cap) 
        st.subheader(eps)
        st.subheader(roe)
        st.subheader(pe) 
        st.subheader(dte) 
        st.subheader(pb)
        st.subheader(ps) 
        st.subheader(peg)
        st.subheader(cr)
        st.subheader(dy)
        st.subheader(insiders)

    #insert graph of close prices
    from datetime import date, timedelta
    import pandas as pd

    st.header("10Y Share Price Chart:")
    today = date.today()
    td = timedelta(3652.5)
    prev_10 = today - td

    data = yf.download(symbol,prev_10,today)

    chart_data = pd.DataFrame(data['Adj Close'])

    st.line_chart(chart_data, width=2000, height=500, use_container_width=True)


    col3, col4 = st.columns(2)
    with col3:
        st.header("Piotroski F-Score is:")
    
    with col4:
        st.header(p_score)
    
    st.caption("Range of this score is of 0-9, where a higher number represents a better stock")
    
    import pyautogui
    
    if st.button("Reset"):
        pyautogui.hotkey("ctrl","F5")

