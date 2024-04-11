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
orcl_yoy_income_stmt = yf.Ticker.get_income_stmt(orcl)

df1 = pd.DataFrame(orcl_yoy_income_stmt)

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

ordered_income_statement = df1.reindex(orcl_desired_index_order)

st.dataframe(
    ordered_income_statement,
    column_config={
        "": st.column_config.Column("Breakdown", width="1800"),
        "2023-05-31 00:00:00": "2023",
        "2022-05-31 00:00:00": "2022",
        "2021-05-31 00:00:00": "2021",
        "2020-05-31 00:00:00": "2020"
    },
    width=1600,
    height=700
)




