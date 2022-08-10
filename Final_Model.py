from app import stock

#calculation of piotroski-F score
import yfinance as yf

stock  = yf.Ticker("AAPL")

info = stock.info

bs = stock.balance_sheet
bs = bs.T

cf = stock.cashflow
cf = cf.T

fin = stock.financials
fin = fin.T

ni = cf["Net Income"][0]

def roa():
    c_tca = bs["Total Current Assets"][0]
    c_tl = bs["Total Liab"][0]
    c_roa = c_tca/c_tl
    return c_roa

def ocf():
    c_ocf = info["operatingCashflow"]
    if isinstance(c_ocf,int) == True:
        return c_ocf
    else:
        return 0
    
def lt_debt():
    try:
        c_lt_debt = bs["Deferred Long Term Liab"][0]
    except KeyError:
        c_lt_debt = 0
    try:
        py_lt_debt = bs["Deferred Long Term Liab"][1]
    except KeyError:
        py_lt_debt = 0

    if c_lt_debt < py_lt_debt:
        return 1
    else:
         return 0
       
def current_ratio():
    c_tca = bs["Total Current Assets"][0]
    py_tca = bs["Total Current Assets"][1]
    c_tl = bs["Total Liab"][0]
    py_tl = bs["Total Liab"][1]
    r1 = c_tca/c_tl
    r2 = py_tca/py_tl
    if r1 > r2:
        return 1
    else:
        return 0
        
def new_shares():
    c_ns = bs['Common Stock'][0]
    py_ns = bs['Common Stock'][1]
    if c_ns - py_ns == 0:
        return 1
    else:
        return 0

def gross_margin():
    c_gm = fin["Gross Profit"][0]
    py_gm = fin["Gross Profit"][1]
    return c_gm - py_gm

def at_ratio():
    c_assets = bs["Total Assets"][0]
    py1_assets = bs["Total Assets"][1]
    py2_assets = bs["Total Assets"][2]
    av1 = (c_assets+py1_assets)/2
    av2 = (py1_assets+py2_assets)/2
    atr1 = fin["Total Revenue"][0]/av1
    atr2 = fin["Total Revenue"][1]/av2
    return atr1-atr2

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
print("")
print("Score is:", p_score )