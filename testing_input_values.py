import streamlit as st 
import numpy as np 
import pandas as pd
import yfinance as yf 

#Create tabs for streamlit application
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Tickers", "Income Statements", "Balance Sheet Statements", "Cash Flow Statements", "Fundamental Ratios"])


# Text Input of Tickers
with tab1:
    company_one = st.text_input('First Ticker')
    company_two = st.text_input('Second Ticker')
    company_three = st.text_input('Third Ticker')
    company_four = st.text_input('Fourth Ticker')
    company_five = st.text_input('Fifth Ticker')
    company_six = st.text_input('Sixth Ticker')
    company_seven = st.text_input('Seventh Ticker')
    company_eight = st.text_input('Eighth Ticker')


#Income Statements
def get_multiple_income_statements(*args):
    income_statements = {}
    for symbol in args:
        ticker = yf.Ticker(symbol)
        income_statements[symbol] = yf.Ticker.get_income_stmt(ticker)
    return income_statements


#Balance Sheet Statements
def get_multiple_balance_sheet_statements(*args):
    income_statements = {}
    for symbol in args:
        ticker = yf.Ticker(symbol)
        income_statements[symbol] = yf.Ticker.get_balance_sheet(ticker)
    return income_statements


# Cash Flow Statements
def get_multiple_cash_flow_statements(*args):
    income_statements = {}
    for symbol in args:
        ticker = yf.Ticker(symbol)
        income_statements[symbol] = yf.Ticker.get_cash_flow(ticker)
    return income_statements


# Calls all statements
multiple_income_statements = get_multiple_income_statements(company_one, company_two, company_three, company_four,
                                                            company_five, company_six, company_seven, company_eight)

multiple_balance_sheet_statements = get_multiple_balance_sheet_statements(company_one, company_two, company_three, company_four,
                                                            company_five, company_six, company_seven, company_eight)

multiple_cash_flow_statements = get_multiple_cash_flow_statements(company_one, company_two, company_three, company_four,
                                                            company_five, company_six, company_seven, company_eight)


# Function to separate dictionary values from values
keys_list = list(multiple_income_statements.keys())


#Desired order for income statement
income_statement_desired_index_order =[
    'TotalRevenue', 'OperatingRevenue', 'CostOfRevenue', 'GrossProfit', 'OperatingExpense', 'SellingGeneralAndAdministration',
    'GeneralAndAdministrativeExpense', 'SalariesAndWages', 'OtherGandA', 'SellingandMarketingExpense', 'ResearchAndDevelopment',
    'DepreciationAmortizationDepletionIncomeStatement', 'DepreciationAndAmortizationInIncomeStatement', 'Amortization', 'AmortizationOfIntangiblesIncomeStatement',
    'OtherOperatingExpenses', 'OperatingIncome', 'NetNonOperatingInterestIncomeExpense', 'InterestIncomeNonOperating', 'InterestExpenseNonOperating',
    'OtherIncomeExpense', 'GainOnSaleOfSecurity', 'EarningsFromEquityInterest', 'SpecialIncomeCharges', 'RestructuringAndMergernAcquisition',
    'OtherNonOperatingIncomeExpenses', 'PretaxIncome', 'TaxProvision', 'NetIncomeCommonStockholders', 'NetIncome', 'NetIncomeIncludingNoncontrollingInterests',
    'NetIncomeFromContinuingAndDiscontinuedOperation', 'DilutedNIAvailtoComStockholders', 'BasicEPS', 'DilutedEPS', 'BasicAverageShares',
    'DilutedAverageShares', 'TotalOperatingIncomeAsReported', 'TotalExpenses', 'NetIncomeFromContinuingOperationNetMinorityInterest',
    'NormalizedIncome', 'InterestIncome', 'InterestExpense', 'NetInterestIncome', 'EBIT', 'EBITDA', 'ReconciledCostofRevenue',
    'ReconciledDepreciation', 'NetIncome', 'NetIncomeFromContinuingOperationNetMinorityInterest', 'TotalUnusualItemsExcludingGoodwill',
    'TotalUnusualItems', 'NormalizedEBITDA', 'TaxRateForCalcs', 'TaxEffectOfUnusualItems'
]



with tab2:
    if len(keys_list) >= 1 and len(list(multiple_income_statements.keys())) >= 1:
        if list(multiple_income_statements.keys())[0] == keys_list[0] and len(list(multiple_income_statements.keys())) >= 1:
            st.dataframe(
                    multiple_income_statements[keys_list[0]].reindex(income_statement_desired_index_order),
                    column_config={
                        "": st.column_config.Column(keys_list[0], width="1800"),
                        "2023-05-31 00:00:00": "2023",
                        "2022-05-31 00:00:00": "2022",
                        "2021-05-31 00:00:00": "2021",
                        "2020-05-31 00:00:00": "2020"
                    },
                    width=1600,
                    height=400
                )
        else:
            pass

    if len(keys_list) >= 2 and len(list(multiple_income_statements.keys())) >= 2:
        if list(multiple_income_statements.keys())[1] == keys_list[1]:
            st.dataframe(
                    multiple_income_statements[keys_list[1]].reindex(income_statement_desired_index_order),
                    column_config={
                        "": st.column_config.Column(keys_list[1], width="1800"),
                        "2023-05-31 00:00:00": "2023",
                        "2022-05-31 00:00:00": "2022",
                        "2021-05-31 00:00:00": "2021",
                        "2020-05-31 00:00:00": "2020"
                    },
                    width=2000,
                    height=400
                )
        else:
            pass

    if len(keys_list) >= 2 and len(list(multiple_income_statements.keys())) >= 2:    
        if list(multiple_income_statements.keys())[2] == keys_list[2]:
            st.dataframe(
                    multiple_income_statements[keys_list[2]].reindex(income_statement_desired_index_order),
                    column_config={
                        "": st.column_config.Column(keys_list[2], width="1800"),
                        "2023-05-31 00:00:00": "2023",
                        "2022-05-31 00:00:00": "2022",
                        "2021-05-31 00:00:00": "2021",
                        "2020-05-31 00:00:00": "2020"
                    },
                    width=1600,
                    height=400
                )
        else:
            pass

    if len(keys_list) >= 2 and len(list(multiple_income_statements.keys())) >= 2:
        if list(multiple_income_statements.keys())[3] == keys_list[3]:
            st.dataframe(
                    multiple_income_statements[keys_list[3]].reindex(income_statement_desired_index_order),
                    column_config={
                        "": st.column_config.Column(keys_list[3], width="1800"),
                        "2023-05-31 00:00:00": "2023",
                        "2022-05-31 00:00:00": "2022",
                        "2021-05-31 00:00:00": "2021",
                        "2020-05-31 00:00:00": "2020"
                    },
                    width=1600,
                    height=400
                )
        else:
            pass

    if len(keys_list) >= 2 and len(list(multiple_income_statements.keys())) >= 2:
        if list(multiple_income_statements.keys())[4] == keys_list[4]:
            st.dataframe(
                    multiple_income_statements[keys_list[4]].reindex(income_statement_desired_index_order),
                    column_config={
                        "": st.column_config.Column(keys_list[4], width="1800"),
                        "2023-05-31 00:00:00": "2023",
                        "2022-05-31 00:00:00": "2022",
                        "2021-05-31 00:00:00": "2021",
                        "2020-05-31 00:00:00": "2020"
                    },
                    width=1600,
                    height=400
                )
        else:
            pass

    if len(keys_list) >= 2 and len(list(multiple_income_statements.keys())) >= 2:        
        if list(multiple_income_statements.keys())[5] == keys_list[5]:
            st.dataframe(
                    multiple_income_statements[keys_list[5]].reindex(income_statement_desired_index_order),
                    column_config={
                        "": st.column_config.Column(keys_list[5], width="1800"),
                        "2023-05-31 00:00:00": "2023",
                        "2022-05-31 00:00:00": "2022",
                        "2021-05-31 00:00:00": "2021",
                        "2020-05-31 00:00:00": "2020"
                    },
                    width=1600,
                    height=400
                )
        else:
            pass
            
    if len(keys_list) >= 2 and len(list(multiple_income_statements.keys())) >= 2:        
        if list(multiple_income_statements.keys())[6] == keys_list[6]:
            st.dataframe(
                    multiple_income_statements[keys_list[6]].reindex(income_statement_desired_index_order),
                    column_config={
                        "": st.column_config.Column(keys_list[6], width="1800"),
                        "2023-05-31 00:00:00": "2023",
                        "2022-05-31 00:00:00": "2022",
                        "2021-05-31 00:00:00": "2021",
                        "2020-05-31 00:00:00": "2020"
                    },
                    width=1600,
                    height=400
                )
        else:
            pass
            
    if len(keys_list) >= 2 and len(list(multiple_income_statements.keys())) >= 2:        
        if list(multiple_income_statements.keys())[7] == keys_list[7]:
            st.dataframe(
                    multiple_income_statements[keys_list[7]].reindex(income_statement_desired_index_order),
                    column_config={
                        "": st.column_config.Column(keys_list[7], width="1800"),
                        "2023-05-31 00:00:00": "2023",
                        "2022-05-31 00:00:00": "2022",
                        "2021-05-31 00:00:00": "2021",
                        "2020-05-31 00:00:00": "2020"
                    },
                    width=1600,
                    height=400
                )
        else:
            pass