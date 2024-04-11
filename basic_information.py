import streamlit as st 
import numpy as np 
import pandas as pd
import yfinance as yf 

#Ticker symbol for Oracle
orcl = yf.Ticker("ORCL")

orcl_yoy_income_stmt = yf.Ticker.get_income_stmt(orcl)

df1 = pd.DataFrame(orcl_yoy_income_stmt)

st.dataframe(df1)




