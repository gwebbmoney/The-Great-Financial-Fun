import streamlit as st 
import numpy as np 
import pandas as pd
import yfinance as yf 

#Ticker symbol for Cloud Services
orcl = yf.Ticker("ORCL")
msft = yf.Ticker("MSFT")
googl = yf.Ticker("GOOGL")
adbe = yf.Ticker('ADBE')
crm = yf.Ticker('CRM')
csco = yf.Ticker('CSCO')
intu = yf.Ticker('INTU')
sap = yf.Ticker('SAP')

#Test
tickers = st.text_input('Input ticker here')

ticker_symbols = tickers


#Income Statements
def get_multiple_income_statements(ticker_symbols):
    income_statements = {}
    for symbol in ticker_symbols:
        ticker = yf.Ticker(symbol)
        income_statements[symbol] = yf.Ticker.get_income_stmt(ticker)
    return income_statements


#Balance Sheet Statements
def get_multiple_balance_sheet_statements(ticker_symbols):
    income_statements = {}
    for symbol in ticker_symbols:
        ticker = yf.Ticker(symbol)
        income_statements[symbol] = yf.Ticker.get_balance_sheet(ticker)
    return income_statements


# Cash Flow Statements
def get_multiple_cash_flow_statements(ticker_symbols):
    income_statements = {}
    for symbol in ticker_symbols:
        ticker = yf.Ticker(symbol)
        income_statements[symbol] = yf.Ticker.get_cash_flow(ticker)
    return income_statements


# Calls all statements
multiple_income_statements = get_multiple_income_statements(ticker_symbols)
multiple_balance_sheet_statements = get_multiple_balance_sheet_statements(ticker_symbols)
multiple_cash_flow_statements = get_multiple_cash_flow_statements(ticker_symbols)

# Function to separate dictionary values from values
def single_income_statement(multiple_income_statements):
    for key in multiple_income_statements.keys():
        return(multiple_income_statements[key])
    
income_statement_few = single_income_statement(multiple_income_statements)
        
for i, df in enumerate(income_statement_few):
    st.write(f"Data {i+1}")
    if isinstance(df, pd.DataFrame):
        st.dataframe(df)
    else:
        st.write(df)



'''
st.dataframe(
        income_statement_few,
        column_config={
            "": st.column_config.Column("Oracle", width="1800"),
            "2023-05-31 00:00:00": "2023",
            "2022-05-31 00:00:00": "2022",
            "2021-05-31 00:00:00": "2021",
            "2020-05-31 00:00:00": "2020"
        },
        width=1600,
        height=400
    )
'''
