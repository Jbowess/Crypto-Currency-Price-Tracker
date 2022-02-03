# Importing

import yfinance as fin
import streamlit as st
import plotly_express as px
import pandas as pd
import calendar

# Webapp title
st.title(''' CryptoCompare
A sophisticated and user-friendly web app that allows you to view your favourite cryptocurrencies in realtime.
''')

# Webapp header for coin board
st.header('''**Live Coin Board**
Select cryptocurrencies through the sidebar on the left.''')

# Importing Crypto Api
Crypto = pd.read_json('https://api.binance.com/api/v3/ticker/24hr')

# If a coin is below 1, determines how many digits to show, returns the values
def round_value(input_value):
    if input_value.values > 1:
        f = float(round(input_value, 2))
    else:
        f = float(round(input_value, 6))
    return f

c1, c2, c3 = st.columns(3)

# Side Bar(Cryptocurrency selection box) (symbol is api call from binance)
coin1 = st.sidebar.selectbox('CryptoCoin 1', Crypto.symbol, list(Crypto.symbol).index('KAVAETH'))

coin2 = st.sidebar.selectbox('CryptoCoin 2', Crypto.symbol, list(Crypto.symbol).index('OAXETH'))

coin3 = st.sidebar.selectbox('CryptoCoin 3', Crypto.symbol, list(Crypto.symbol).index('DOGEBUSD'))

coin4 = st.sidebar.selectbox('CryptoCoin 4', Crypto.symbol, list(Crypto.symbol).index('BQXETH'))

coin5 = st.sidebar.selectbox('CryptoCoin 5', Crypto.symbol, list(Crypto.symbol).index('BTCBUSD'))

coin6 = st.sidebar.selectbox('CryptoCoin 6', Crypto.symbol, list(Crypto.symbol).index('ETHBUSD'))

# Connecting the live board and values of the sidebar
value1 = Crypto[Crypto.symbol == coin1]
value2 = Crypto[Crypto.symbol == coin2]
value3 = Crypto[Crypto.symbol == coin3]
value4 = Crypto[Crypto.symbol == coin4]
value5 = Crypto[Crypto.symbol == coin5]
value6 = Crypto[Crypto.symbol == coin6]


# Detailed description of live coin board
st.subheader("Detailed Board View")
st.write(value1)
st.write(value2)
st.write(value3)
st.write(value4)
st.write(value5)
st.write(value6)


# Rounding the coin values from api value weightedAvgPrice
coin1value = round_value(value1.weightedAvgPrice)
coin2value = round_value(value2.weightedAvgPrice)
coin3value = round_value(value3.weightedAvgPrice)
coin4value = round_value(value4.weightedAvgPrice)
coin5value = round_value(value5.weightedAvgPrice)
coin6value = round_value(value6.weightedAvgPrice)


# Gathering the priceChangePercent from the api call and turning it into a value
col1_percent = f'{float(value1.priceChangePercent)}%'
col2_percent = f'{float(value2.priceChangePercent)}%'
col3_percent = f'{float(value3.priceChangePercent)}%'
col4_percent = f'{float(value4.priceChangePercent)}%'
col5_percent = f'{float(value5.priceChangePercent)}%'
col6_percent = f'{float(value6.priceChangePercent)}%'


# Basic layout for column display, including all prices and %'s corresponding
# with whats been selected on the sidebar
c1.metric(coin1, coin1value, col1_percent)
c2.metric(coin2, coin2value, col2_percent)
c3.metric(coin3, coin3value, col3_percent)
c1.metric(coin4, coin4value, col4_percent)
c2.metric(coin5, coin5value, col5_percent)
c3.metric(coin6, coin6value, col6_percent)


# Ethereum Data from yfinance
st.header("Popular CryptoCurrencies")
st.subheader("ETHEREUM ($USD)")
Ethereum = 'ETH-USD'
ETHDATA = fin.Ticker(Ethereum)
ETH = fin.download(Ethereum, start="2022-1-31", end="2022-2-2")

ETHCoinSummary = ETHDATA.history(period="max")
st.line_chart(ETHCoinSummary.Close)
st.dataframe(ETH)


# BitCoin Data from yfinance
st.subheader("BITCOIN ($USD)")
Bitcoin = 'BTC-USD'
BTCDATA = fin.Ticker(Bitcoin)
BTC = fin.download(Bitcoin, start="2022-1-31", end="2022-2-2")

BTCCoinSummary = BTCDATA.history(period="max")
st.line_chart(BTCCoinSummary.Close)
st.dataframe(BTC)


# Binance Data from yfinance
st.subheader("Binance ($USD)")
Binance = 'BNB-USD'
BNBDATA = fin.Ticker(Binance)
BNB = fin.download(Binance, start="2022-1-31", end="2022-2-2")

BNBCoinSummary = BNBDATA.history(period="max")
st.line_chart(BNBCoinSummary.Close)
st.dataframe(BNB)

# AUD Conversion Rate from USD
st.header("USD to AUD Conversion")

# ETH
st.subheader("ETH")
ETHAUD = fin.download(Ethereum, start="2022-2-2", end="2022-2-2")
ETHUSD = fin.download(Ethereum, start="2022-2-2", end="2022-2-2")
st.caption("USD")
st.table(ETHUSD)
st.caption("AUD")
st.table(ETHAUD * 1.4)

# BTC
st.subheader("BTC")
BTCAUD = fin.download(Bitcoin, start="2022-2-2", end="2022-2-2")
BTCUSD = fin.download(Bitcoin, start="2022-2-2", end="2022-2-2")
st.caption("USD")
st.table(BTCUSD)
st.caption("AUD")
st.table(BTCAUD * 1.4)

# BNB
st.subheader("BNB")
BNBAUD = fin.download(Binance, start="2022-2-2", end="2022-2-2")
BNBUSD = fin.download(Binance, start="2022-2-2", end="2022-2-2")
st.caption("USD")
st.table(BNBUSD)
st.caption("AUD")
st.table(BNBAUD * 1.4)