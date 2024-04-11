import streamlit as st 
import numpy as np 
import pandas as pd
import yfinance as yf 

#Ticker symbol for Oracle
orcl = yf.Ticker("ORCL")

orcl_yoy_income_stmt = yf.Ticker.get_income_stmt(orcl)

df1 = pd.DataFrame(orcl_yoy_income_stmt)

#Desired order for income statement
desired_index_order =[
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

ordered_income_statement = df1.reindex(desired_index_order)

st.dataframe(
    ordered_income_statement,
    column_config={
        "": st.column_config.Column("Breakdown", width="1400"),
        "2023-05-31 00:00:00": "2023",
        "2022-05-31 00:00:00": "2022",
        "2021-05-31 00:00:00": "2021",
        "2020-05-31 00:00:00": "2020"
    },
    width=1200,
    height=1200
)




