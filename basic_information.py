import streamlit as st 
import numpy as np 
import pandas as pd
import yfinance as yf 

#Ticker symbol for Oracle
orcl = yf.Ticker("ORCL")
msft = yf.Ticker("MSFT")
googl = yf.Ticker("GOOGL")
adbe = yf.Ticker('ADBE')
crm = yf.Ticker('CRM')
csco = yf.Ticker('CSCO')
intu = yf.Ticker('INTU')
sap = yf.Ticker('SAP')

#Income Statements
def get_multiple_income_statements(ticker_symbols):
    income_statements = {}
    for symbol in ticker_symbols:
        ticker = yf.Ticker(symbol)
        income_statements[symbol] = yf.Ticker.get_income_stmt(ticker)
    return income_statements

ticker_symbols = ['ORCL', 'MSFT', 'GOOGL', 'ADBE', 'CRM', 'CSCO', 'INTU', 'SAP']

income_statements = get_multiple_income_statements(ticker_symbols)

# Calculate profitability ratios
def gross_margin(income_statements):
    grossmargin = {}
    for keys in income_statements.keys():
        grossmargin[keys] = income_statements[keys].loc['GrossProfit']/income_statements[keys].loc['TotalRevenue']
        grossmargin[keys].index = grossmargin[keys].index.strftime('%Y')
    df1 = pd.DataFrame(grossmargin)
    df1_transpose = df1.transpose()
    return(df1_transpose)

def operating_margin(income_statements):
    grossmargin = {}
    for keys in income_statements.keys():
        grossmargin[keys] = income_statements[keys].loc['OperatingIncome']/income_statements[keys].loc['TotalRevenue']
        grossmargin[keys].index = grossmargin[keys].index.strftime('%Y')
    df1 = pd.DataFrame(grossmargin)
    df1_transpose = df1.transpose()
    return(df1_transpose)

def ebitda_margin(income_statements):
    grossmargin = {}
    for keys in income_statements.keys():
        grossmargin[keys] = income_statements[keys].loc['EBITDA']/income_statements[keys].loc['TotalRevenue']
        grossmargin[keys].index = grossmargin[keys].index.strftime('%Y')
    df1 = pd.DataFrame(grossmargin)
    df1_transpose = df1.transpose()
    return(df1_transpose)

def ebit_margin(income_statements):
    grossmargin = {}
    for keys in income_statements.keys():
        grossmargin[keys] = income_statements[keys].loc['EBIT']/income_statements[keys].loc['TotalRevenue']
        grossmargin[keys].index = grossmargin[keys].index.strftime('%Y')
    df1 = pd.DataFrame(grossmargin)
    df1_transpose = df1.transpose()
    return(df1_transpose)

def net_profit_margin(income_statements):
    grossmargin = {}
    for keys in income_statements.keys():
        grossmargin[keys] = income_statements[keys].loc['NetIncome']/income_statements[keys].loc['TotalRevenue']
        grossmargin[keys].index = grossmargin[keys].index.strftime('%Y')
    df1 = pd.DataFrame(grossmargin)
    df1_transpose = df1.transpose()
    return(df1_transpose)

#Desired order for income statement
orcl_desired_index_order =[
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

msft_desired_index_order = [
    'TotalRevenue', 'OperatingRevenue', 'CostOfRevenue', 'GrossProfit', 'OperatingExpense', 'SellingGeneralAndAdministration',
    'GeneralAndAdministrativeExpense', 'SalariesAndWages', 'OtherGandA', 'SellingandMarketingExpense', 'ResearchAndDevelopment',
    'OperatingIncome', 'NetNonOperatingInterestIncomeExpense', 'InterestIncomeNonOperating', 'InterestExpenseNonOperating',
    'OtherIncomeExpense', 'GainOnSaleOfSecurity', 'SpecialIncomeCharges', 'WriteOff', 'OtherNonOperatingIncomeExpenses', 
    'PretaxIncome', 'TaxProvision', 'NetIncomeCommonStockholders', 'NetIncome', 'NetIncomeIncludingNoncontrollingInterests',
    'NetIncomeContinuousOperations', 'DilutedNIAvailtoComStockholders', 'BasicEPS', 'DilutedEPS', 'BasicAverageShares',
    'DilutedAverageShares', 'TotalOperatingIncomeAsReported', 'TotalExpenses', 'NetIncomeFromContinuingAndDiscontinuedOperation',
    'NormalizedIncome', 'InterestIncome', 'InterestExpense', 'NetInterestIncome', 'EBIT', 'EBITDA','ReconciledCostofRevenue',
    'ReconciledDepreciation', 'NetIncome', 'NetIncomeFromContinuingOperationNetMinorityInterest', 'TotalUnusualItemsExcludingGoodwill',
    'TotalUnusualItems', 'NormalizedEBITDA', 'TaxRateForCalcs', 'TaxEffectOfUnusualItems'
]

googl_desired_index_order = [ 'TotalRevenue', 'OperatingRevenue', 'CostOfRevenue', 'GrossProfit', 'OperatingExpense', 'SellingGeneralAndAdministration',
    'GeneralAndAdministrativeExpense', 'SalariesAndWages', 'OtherGandA', 'SellingandMarketingExpense', 'ResearchAndDevelopment',
    'OperatingIncome', 'NetNonOperatingInterestIncomeExpense', 'InterestIncomeNonOperating', 'InterestExpenseNonOperating',
    'OtherIncomeExpense', 'GainOnSaleOfSecurity', 'SpecialIncomeCharges', 'WriteOff', 'OtherNonOperatingIncomeExpenses', 
    'PretaxIncome', 'TaxProvision', 'NetIncomeCommonStockholders', 'NetIncome', 'NetIncomeIncludingNoncontrollingInterests',
    'NetIncomeContinuousOperations', 'DilutedNIAvailtoComStockholders', 'BasicEPS', 'DilutedEPS', 'BasicAverageShares',
    'DilutedAverageShares', 'TotalOperatingIncomeAsReported', 'TotalExpenses', 'NetIncomeFromContinuingAndDiscontinuedOperation',
    'NormalizedIncome', 'InterestIncome', 'InterestExpense', 'NetInterestIncome', 'EBIT', 'EBITDA','ReconciledCostofRevenue',
    'ReconciledDepreciation', 'NetIncome', 'NetIncomeFromContinuingOperationNetMinorityInterest', 'TotalUnusualItemsExcludingGoodwill',
    'TotalUnusualItems', 'NormalizedEBITDA', 'TaxRateForCalcs', 'TaxEffectOfUnusualItems'
]

adbe_desired_index_order = [ 'TotalRevenue', 'OperatingRevenue', 'CostOfRevenue', 'GrossProfit', 'OperatingExpense', 'SellingGeneralAndAdministration',
    'GeneralAndAdministrativeExpense', 'SalariesAndWages', 'OtherGandA', 'SellingandMarketingExpense', 'ResearchAndDevelopment',
    'OperatingIncome', 'NetNonOperatingInterestIncomeExpense', 'InterestIncomeNonOperating', 'InterestExpenseNonOperating',
    'OtherIncomeExpense', 'GainOnSaleOfSecurity', 'SpecialIncomeCharges', 'WriteOff', 'OtherNonOperatingIncomeExpenses', 
    'PretaxIncome', 'TaxProvision', 'NetIncomeCommonStockholders', 'NetIncome', 'NetIncomeIncludingNoncontrollingInterests',
    'NetIncomeContinuousOperations', 'DilutedNIAvailtoComStockholders', 'BasicEPS', 'DilutedEPS', 'BasicAverageShares',
    'DilutedAverageShares', 'TotalOperatingIncomeAsReported', 'TotalExpenses', 'NetIncomeFromContinuingAndDiscontinuedOperation',
    'NormalizedIncome', 'InterestIncome', 'InterestExpense', 'NetInterestIncome', 'EBIT', 'EBITDA','ReconciledCostofRevenue',
    'ReconciledDepreciation', 'NetIncome', 'NetIncomeFromContinuingOperationNetMinorityInterest', 'TotalUnusualItemsExcludingGoodwill',
    'TotalUnusualItems', 'NormalizedEBITDA', 'TaxRateForCalcs', 'TaxEffectOfUnusualItems'
]

crm_desired_index_order = ['TotalRevenue', 'OperatingRevenue', 'CostOfRevenue', 'GrossProfit', 'OperatingExpense', 'SellingGeneralAndAdministration',
    'GeneralAndAdministrativeExpense', 'SalariesAndWages', 'OtherGandA', 'SellingandMarketingExpense', 'ResearchAndDevelopment',
    'OperatingIncome', 'NetNonOperatingInterestIncomeExpense', 'InterestIncomeNonOperating', 'InterestExpenseNonOperating',
    'OtherIncomeExpense', 'GainOnSaleOfSecurity', 'SpecialIncomeCharges', 'WriteOff', 'OtherNonOperatingIncomeExpenses', 
    'PretaxIncome', 'TaxProvision', 'NetIncomeCommonStockholders', 'NetIncome', 'NetIncomeIncludingNoncontrollingInterests',
    'NetIncomeContinuousOperations', 'DilutedNIAvailtoComStockholders', 'BasicEPS', 'DilutedEPS', 'BasicAverageShares',
    'DilutedAverageShares', 'TotalOperatingIncomeAsReported', 'TotalExpenses', 'NetIncomeFromContinuingAndDiscontinuedOperation',
    'NormalizedIncome', 'InterestIncome', 'InterestExpense', 'NetInterestIncome', 'EBIT', 'EBITDA','ReconciledCostofRevenue',
    'ReconciledDepreciation', 'NetIncome', 'NetIncomeFromContinuingOperationNetMinorityInterest', 'TotalUnusualItemsExcludingGoodwill',
    'TotalUnusualItems', 'NormalizedEBITDA', 'TaxRateForCalcs', 'TaxEffectOfUnusualItems'
]

csco_desired_index_order = ['TotalRevenue', 'OperatingRevenue', 'CostOfRevenue', 'GrossProfit', 'OperatingExpense', 'SellingGeneralAndAdministration',
    'GeneralAndAdministrativeExpense', 'SalariesAndWages', 'OtherGandA', 'SellingandMarketingExpense', 'ResearchAndDevelopment',
    'OperatingIncome', 'NetNonOperatingInterestIncomeExpense', 'InterestIncomeNonOperating', 'InterestExpenseNonOperating',
    'OtherIncomeExpense', 'GainOnSaleOfSecurity', 'SpecialIncomeCharges', 'WriteOff', 'OtherNonOperatingIncomeExpenses', 
    'PretaxIncome', 'TaxProvision', 'NetIncomeCommonStockholders', 'NetIncome', 'NetIncomeIncludingNoncontrollingInterests',
    'NetIncomeContinuousOperations', 'DilutedNIAvailtoComStockholders', 'BasicEPS', 'DilutedEPS', 'BasicAverageShares',
    'DilutedAverageShares', 'TotalOperatingIncomeAsReported', 'TotalExpenses', 'NetIncomeFromContinuingAndDiscontinuedOperation',
    'NormalizedIncome', 'InterestIncome', 'InterestExpense', 'NetInterestIncome', 'EBIT', 'EBITDA','ReconciledCostofRevenue',
    'ReconciledDepreciation', 'NetIncome', 'NetIncomeFromContinuingOperationNetMinorityInterest', 'TotalUnusualItemsExcludingGoodwill',
    'TotalUnusualItems', 'NormalizedEBITDA', 'TaxRateForCalcs', 'TaxEffectOfUnusualItems'
]

intu_desired_index_order = ['TotalRevenue', 'OperatingRevenue', 'CostOfRevenue', 'GrossProfit', 'OperatingExpense', 'SellingGeneralAndAdministration',
    'GeneralAndAdministrativeExpense', 'SalariesAndWages', 'OtherGandA', 'SellingandMarketingExpense', 'ResearchAndDevelopment',
    'OperatingIncome', 'NetNonOperatingInterestIncomeExpense', 'InterestIncomeNonOperating', 'InterestExpenseNonOperating',
    'OtherIncomeExpense', 'GainOnSaleOfSecurity', 'SpecialIncomeCharges', 'WriteOff', 'OtherNonOperatingIncomeExpenses', 
    'PretaxIncome', 'TaxProvision', 'NetIncomeCommonStockholders', 'NetIncome', 'NetIncomeIncludingNoncontrollingInterests',
    'NetIncomeContinuousOperations', 'DilutedNIAvailtoComStockholders', 'BasicEPS', 'DilutedEPS', 'BasicAverageShares',
    'DilutedAverageShares', 'TotalOperatingIncomeAsReported', 'TotalExpenses', 'NetIncomeFromContinuingAndDiscontinuedOperation',
    'NormalizedIncome', 'InterestIncome', 'InterestExpense', 'NetInterestIncome', 'EBIT', 'EBITDA','ReconciledCostofRevenue',
    'ReconciledDepreciation', 'NetIncome', 'NetIncomeFromContinuingOperationNetMinorityInterest', 'TotalUnusualItemsExcludingGoodwill',
    'TotalUnusualItems', 'NormalizedEBITDA', 'TaxRateForCalcs', 'TaxEffectOfUnusualItems'
]

sap_desired_index_order = ['TotalRevenue', 'OperatingRevenue', 'CostOfRevenue', 'GrossProfit', 'OperatingExpense', 'SellingGeneralAndAdministration',
    'GeneralAndAdministrativeExpense', 'SalariesAndWages', 'OtherGandA', 'SellingandMarketingExpense', 'ResearchAndDevelopment',
    'OperatingIncome', 'NetNonOperatingInterestIncomeExpense', 'InterestIncomeNonOperating', 'InterestExpenseNonOperating',
    'OtherIncomeExpense', 'GainOnSaleOfSecurity', 'SpecialIncomeCharges', 'WriteOff', 'OtherNonOperatingIncomeExpenses', 
    'PretaxIncome', 'TaxProvision', 'NetIncomeCommonStockholders', 'NetIncome', 'NetIncomeIncludingNoncontrollingInterests',
    'NetIncomeContinuousOperations', 'DilutedNIAvailtoComStockholders', 'BasicEPS', 'DilutedEPS', 'BasicAverageShares',
    'DilutedAverageShares', 'TotalOperatingIncomeAsReported', 'TotalExpenses', 'NetIncomeFromContinuingAndDiscontinuedOperation',
    'NormalizedIncome', 'InterestIncome', 'InterestExpense', 'NetInterestIncome', 'EBIT', 'EBITDA','ReconciledCostofRevenue',
    'ReconciledDepreciation', 'NetIncome', 'NetIncomeFromContinuingOperationNetMinorityInterest', 'TotalUnusualItemsExcludingGoodwill',
    'TotalUnusualItems', 'NormalizedEBITDA', 'TaxRateForCalcs', 'TaxEffectOfUnusualItems'
]

#All income statements
orcl_income_statement = income_statements['ORCL'].reindex(orcl_desired_index_order)
msft_income_statement = income_statements['MSFT'].reindex(msft_desired_index_order)
googl_income_statement = income_statements['GOOGL'].reindex(googl_desired_index_order)
adbe_income_statement = income_statements['ADBE'].reindex(adbe_desired_index_order)
crm_income_statement = income_statements['CRM'].reindex(crm_desired_index_order)
csco_income_statement = income_statements['CSCO'].reindex(csco_desired_index_order)
intu_income_statement = income_statements['INTU'].reindex(csco_desired_index_order)
sap_income_statement = income_statements['SAP'].reindex(csco_desired_index_order)


tab1, tab2, tab3, tab4 = st.tabs(["Income Statements", "Balance Sheet Statements", "Cash Flow Statements", "Fundamental Ratios"])

with tab1:
    st.dataframe(
        orcl_income_statement,
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

    st.dataframe(
        msft_income_statement,
        column_config={
            "": st.column_config.Column("Microsoft", width="1800"),
            "2023-06-30 00:00:00": "2023",
            "2022-06-30 00:00:00": "2022",
            "2021-06-30 00:00:00": "2021",
            "2020-06-30 00:00:00": "2020"
        },
        width=1600,
        height=400
    )

    st.dataframe(
        googl_income_statement,
        column_config={
            "": st.column_config.Column("Google", width="1800"),
            "2023-12-31 00:00:00": "2023",
            "2022-12-31 00:00:00": "2022",
            "2021-12-31 00:00:00": "2021",
            "2020-12-31 00:00:00": "2020"
        },
        width=1600,
        height=400
    )

    st.dataframe(
        adbe_income_statement,
        column_config={
            "": st.column_config.Column("Adobe", width="1800"),
            "2023-11-30 00:00:00": "2023",
            "2022-11-30 00:00:00": "2022",
            "2021-11-30 00:00:00": "2021",
            "2020-11-30 00:00:00": "2020"
        },
        width=1600,
        height=400
    )

    st.dataframe(
        crm_income_statement,
        column_config={
            "": st.column_config.Column("Salesforce", width="1800"),
            "2024-01-31 00:00:00": "2023",
            "2022-01-31 00:00:00": "2022",
            "2021-01-31 00:00:00": "2021",
            "2020-01-31 00:00:00": "2020"
        },
        width=1600,
        height=400
    )

    st.dataframe(
        csco_income_statement,
        column_config={
            "": st.column_config.Column("Cisco", width="1800"),
            "2023-07-31 00:00:00": "2023",
            "2022-07-31 00:00:00": "2022",
            "2021-07-31 00:00:00": "2021",
            "2020-07-31 00:00:00": "2020"
        },
        width=1600,
        height=400
    )

    st.dataframe(
        intu_income_statement,
        column_config={
            "": st.column_config.Column("Intuit", width="1800"),
            "2023-07-31 00:00:00": "2023",
            "2022-07-31 00:00:00": "2022",
            "2021-07-31 00:00:00": "2021",
            "2020-07-31 00:00:00": "2020"
        },
        width=1600,
        height=400
    )

    st.dataframe(
        sap_income_statement,
        column_config={
            "": st.column_config.Column("SAP", width="1800"),
            "2023-12-31 00:00:00": "2023",
            "2022-12-31 00:00:00": "2022",
            "2021-12-31 00:00:00": "2021",
            "2020-12-31 00:00:00": "2020"
        },
        width=1600,
        height=400
    )

with tab4:
    col1, col2 = st.columns(2)
    col1.subheader("Gross Margin")
    col1.dataframe(gross_margin(income_statements))

    col2.subheader("Operating Margin")
    col2.dataframe(operating_margin(income_statements))

    col3, col4 = st.columns(2)
    col3.subheader("EBITDA Margin")
    col3.dataframe(ebitda_margin(income_statements))

    col4.subheader("EBIT Margin")
    col4.dataframe(ebit_margin(income_statements))

    col5, col6 = st.columns(2)
    col5.subheader("Net Profit Margin")
    col5.dataframe(net_profit_margin(income_statements))
