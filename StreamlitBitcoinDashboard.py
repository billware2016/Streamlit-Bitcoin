import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen
from datetime import datetime

# Titles and subtitles
st.title("Cryptocurrency Daily Prices")
st.header("My Dashboard")


# Defining ticker variables
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'

# Access data from Yahoo finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)

# Fetch History data from Yahoo Finance
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")

# Fetch crypto data for the dataframe
end_date = datetime.now().strftime('%Y-%m-%d')
BTC = yf.download(Bitcoin, start="2024-2-29",
                  end=end_date)
ETH = yf.download(Ethereum, start="2024-2-29",
                  end=end_date)

# Bitcoin
st.write("BITCOIN ($)")
imageBTC = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1.png"))
#Display image
st.image(imageBTC)
# Display dataframe
st.table(BTC)
# Display a chart
st.bar_chart(BTCHis.Close)

# Ethereum
st.write("ETHEREUM ($)")
imageETH = Image.open(urlopen("https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png"))
#Display image
st.image(imageETH)
# Display dataframe
st.table(ETH)
# Display a chart
st.bar_chart(ETHHis.Close)


