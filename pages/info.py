import streamlit as st

st.title("Information")
st.caption("Ideally one must use these metrics while comparing two or more stocks from the same sector/industry.")

st.header("Previous Close:")
st.write("It is the previous day's final price of the stock when the market closes for the day, officially.")

st.header("Market Cap(italization):")
st.write("It is the total value of a company's shares held in the open market; therefore, it measures how much a company is worth in the stock market.")

st.header("EPS:")
st.write("Earnings Per Share is the company's profit divided by the number of shares of the stock, thus is an indicator of a company's profitability.\nThe higher a company's EPS, the more profitable it is.")

st.header("RoE:")
st.write("Return on Equity is calculated by dividing the net income by shareholders' equity.\nIt is considered a gauge of a company's profitability and efficiency in generating profits.\nThe higher a company's RoE, the more efficient it is at generating income from its equity financing.")

st.header("P/E Ratio:")
st.write("Price to Earnings Ratio calculates the current share price relative to its EPS.\n A high P/E ratio could indicate that a company's stock is overvalued.")

st.header("Debt/Equity Ratio:")
st.write("Debt to Equity Ratio is calculated by dividing the company's total liabilities by its shareholder equity.\n A higher Debt/Equity ratio is considered risky.")

st.header("P/B Ratio:")
st.write("Price to Book Ratio is calculated by dividing the current price of the stock by the book value per share.\nGenerally, a lower P/B ratio could mean that the stock is undervalued.")

st.header("P/S Ratio:")
st.write("Price to Sales Ratio measures the price of a company's stock against its annual sales.\n Lower P/S Ratios are favourable.")

st.header("PEG Ratio:")
st.write("Price/Earnings-to-Growth Ratio is a stock's P/E ratio divided by the growth rate of its earnings.\n It indicates a stock's true value.\n A lower PEG may indicate that a stock is undervalued.")

st.header("Current Ratio:")
st.write("It compares all of a company's current assets to its current liabilities. It helps investors understand more about a company's ability to cover its short-term debt with its current assets.\n Usually, a Current Ratio of 1 or higher is considered good.")

st.header("Dividend Yield:")
st.write("It is the amount of money a company pays shareholders for owning a share of its stock divided by its current stock price.\n If one is investing in growth stocks, they must not require a high dividend yield.\n Generally, only mature companies provide high dividends.")

st.header("% Of Insider Stake:")
st.write("This shows how much of majority stake a particular insider has in the company. \n Large companies having 5% is usually significant.\n Although having a higher percentage, say 40%, shows that the management in that company has more stake, thus more control.")

st.header("Piotroski F-Score:")
st.write("It determines the strength of a firm's financial position, thus determines the best value stocks.\n The score ranges from 0-9, where 9 is the best and 0 the worst.")
st.write("Using 9 categories it awards 1 point to a stock if it fulfils that category:")
st.write("1.Positive net income.")
st.write("2.Positive return on assets (ROA) in the current year.")
st.write("3.Positive operating cash flow in the current year.")
st.write("4.Cash flow from operations being greater than net Income (quality of earnings).")
st.write("5.Lower amount of long-term debt in the current period, compared to the previous year (decreased leverage).")
st.write("6.Higher current ratio this year compared to the previous year (more liquidity).")
st.write("7.No new shares were issued in the last year (lack of dilution).")
st.write("8.A higher gross margin compared to the previous year.")
st.write("9.A higher asset turnover ratio compared to the previous year.")