import streamlit as st 
import numpy as np 
import pandas as pd
import yfinance as yf 

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


# All ticker symbols to be analyzed
ticker_symbols = ['ORCL', 'MSFT', 'GOOGL', 'ADBE', 'CRM', 'CSCO', 'INTU', 'SAP']

# Calls all statements
income_statements = get_multiple_income_statements(ticker_symbols)
balance_sheet_statements = get_multiple_balance_sheet_statements(ticker_symbols)
cash_flow_statements = get_multiple_cash_flow_statements(ticker_symbols)


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


# Calculate liquidity ratios
def working_capital_ratio(balance_sheet):
    working_capital = {}
    for keys in balance_sheet.keys():
        working_capital[keys] = balance_sheet[keys].loc['CurrentAssets']/balance_sheet[keys].loc['CurrentLiabilities']
        working_capital[keys].index = working_capital[keys].index.strftime('%Y')
    df1 = pd.DateFrame(working_capital)
    df1_transpose = df1.transpose()
    return(df1_transpose)



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

#All income statements
orcl_income_statement = income_statements['ORCL'].reindex(income_statement_desired_index_order)
msft_income_statement = income_statements['MSFT'].reindex(income_statement_desired_index_order)
googl_income_statement = income_statements['GOOGL'].reindex(income_statement_desired_index_order)
adbe_income_statement = income_statements['ADBE'].reindex(income_statement_desired_index_order)
crm_income_statement = income_statements['CRM'].reindex(income_statement_desired_index_order)
csco_income_statement = income_statements['CSCO'].reindex(income_statement_desired_index_order)
intu_income_statement = income_statements['INTU'].reindex(income_statement_desired_index_order)
sap_income_statement = income_statements['SAP'].reindex(income_statement_desired_index_order)


#Desired order of balance sheet
balance_sheet_index_order = [
    'TotalAssets', 'CurrentAssets', 'CashAndCashEquivalents', 'CashEquivalents', 'Receivables', 'AccountsReceivable', 'PrepaidAssets',
    'OtherCurrentAssets', 'TotalNonCurrentAssets','NetPPE', 'GoodwillAndOtherIntangibleAssets', 'NonCurrentDeferredAssets', 'OtherNonCurrentAssets',
    'TotalLiabilitiesNetMinorityInterest', 'CurrentLiabilities', 'PayablesAndAccruedExpenses', 'Payables', 'AccountsPayable', 'PensionandOtherPostRetirementBenefitPlansCurrent',
    'CurrentDebtAndCapitalLeaseObligation', 'CurrentDebt', 'CurrentDeferredLiabilities', 'OtherCurrentLiabilities','TotalNonCurrentLiabilitiesNetMinorityInterest',
    'LongTermDebtAndCapitalLeaseObligation', 'LongTermDebt', 'NonCurrentDeferredLiabilities', 'TradeandOtherPayablesNonCurrent', 'OtherNonCurrentLiabilities',
    'TotalEquityGrossMinorityInterest', 'StockholdersEquity', 'CapitalStock' ,'CommonStock', 'RetainedEarnings', 'GainsLossesNotAffectingRetainedEarnings',
    'MinorityInterest', 'TotalCapitalization', 'CommonStockEquity', 'NetTangibleAssets', 'WorkingCapital', 'InvestedCapital', 'TangibleBookValue', 'TotalDebt',
    'NetDebt', 'ShareIssued', 'OrdinarySharesNumber'
]


#All balance sheet statements
orcl_balance_sheet_statement = balance_sheet_statements['ORCL'].reindex(balance_sheet_index_order)
msft_balance_sheet_statement = balance_sheet_statements['MSFT'].reindex(balance_sheet_index_order)
googl_balance_sheet_statement = balance_sheet_statements['GOOGL'].reindex(balance_sheet_index_order)
adbe_balance_sheet_statement = balance_sheet_statements['ADBE'].reindex(balance_sheet_index_order)
crm_balance_sheet_statement = balance_sheet_statements['CRM'].reindex(balance_sheet_index_order)
csco_balance_sheet_statement = balance_sheet_statements['CSCO'].reindex(balance_sheet_index_order)
intu_balance_sheet_statement = balance_sheet_statements['INTU'].reindex(balance_sheet_index_order)
sap_balance_sheet_statement = balance_sheet_statements['SAP'].reindex(balance_sheet_index_order)


#Desired order of cash flow statement
cash_flow_statement_index_order = [
    'OperatingCashFlow', 'CashFlowFromContinuingOperatingActivities', 'NetIncomeFromContinuingOperations', 'DepreciationAmortizationDepletion' ,'DepreciationAndAmortization',
    'Depreciation', 'AmortizationCashFlow', 'AmortizationOfIntangibles', 'DeferredTax', 'DeferredIncomeTax', 'ProvisionandWriteOffofAssets', 'StockBasedCompensation',
    'OtherNonCashItems', 'ChangeInWorkingCapital', 'ChangeInReceivables', 'ChangesInAccountReceivables', 'ChangeInPrepaidAssets', 'ChangeInAccountPayable',
    'ChangeInPayable', 'ChangeInTaxPayable', 'ChangeInIncomeTaxPayable', 'ChangeInAccountPayable', 'ChangeInOtherWorkingCapital', 'InvestingCashFlow', 'CashFlowFromContinuingInvestingActivities',
    'CapitalExpenditureReported', 'NetBusinessPurchaseAndSale', 'PurchaseOfBusiness', 'NetInvestmentPurchaseAndSale', 'PurchaseOfInvestment', 'SaleOfInvestment',
    'FinancingCashFlow', 'CashFlowFromContinuingFinancingActivities', 'NetIssuancePaymentsOfDebt', 'NetLongTermDebtIssuance', 'LongTermDebtIssuance', 'LongTermDebtPayments',
    'NetShortTermDebtIssuance', 'ShortTermDebtIssuance', 'NetCommonStockIssuance', 'CommonStockIssuance', 'CommonStockPayments', 'CashDividendsPaid', 'CommonStockDividendPaid',
    'NetOtherFinancingCharges', 'EndCashPosition', 'ChangesInCash', 'EffectOfExchangeRateChanges', 'BeginningCashPosition', 'IncomeTaxPaidSupplementalData', 'InterestPaidSupplementalData',
    'CapitalExpenditure', 'IssuanceOfCapitalStock', 'IssuanceOfDebt', 'RepaymentOfDebt', 'RepurchaseOfCapitalStock', 'FreeCashFlow'
]


#All cash flow statements
orcl_cash_flow_statement = cash_flow_statements['ORCL'].reindex(cash_flow_statement_index_order)
msft_cash_flow_statement = cash_flow_statements['MSFT'].reindex(cash_flow_statement_index_order)
googl_cash_flow_statement = cash_flow_statements['GOOGL'].reindex(cash_flow_statement_index_order)
adbe_cash_flow_statement = cash_flow_statements['ADBE'].reindex(cash_flow_statement_index_order)
crm_cash_flow_statement = cash_flow_statements['CRM'].reindex(cash_flow_statement_index_order)
csco_cash_flow_statement = cash_flow_statements['CSCO'].reindex(cash_flow_statement_index_order)
intu_cash_flow_statement = cash_flow_statements['INTU'].reindex(cash_flow_statement_index_order)
sap_cash_flow_statement = cash_flow_statements['SAP'].reindex(cash_flow_statement_index_order)


#Create tabs for streamlit application
tab1, tab2, tab3, tab4 = st.tabs(["Income Statements", "Balance Sheet Statements", "Cash Flow Statements", "Fundamental Ratios"])


# First tab is annual income statements by ticker symbol
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


# Second tab is annual balance sheet statements by ticker symbol
with tab2:
    st.dataframe(
        orcl_balance_sheet_statement,
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
        msft_balance_sheet_statement,
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
        googl_balance_sheet_statement,
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
        adbe_balance_sheet_statement,
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
        crm_balance_sheet_statement,
        column_config={
            "": st.column_config.Column("Salesforce", width="1800"),
            "2024-01-31 00:00:00": "2024",
            "2023-01-31 00:00:00": "2023",
            "2022-01-31 00:00:00": "2022",
            "2021-01-31 00:00:00": "2021"
        },
        width=1600,
        height=400
    )

    st.dataframe(
        csco_balance_sheet_statement,
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
        intu_balance_sheet_statement,
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
        sap_balance_sheet_statement,
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

# Cash flow statement visualization
with tab3:
    st.dataframe(
        orcl_cash_flow_statement,
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
        msft_cash_flow_statement,
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
        googl_cash_flow_statement,
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
        adbe_cash_flow_statement,
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
        crm_cash_flow_statement,
        column_config={
            "": st.column_config.Column("Salesforce", width="1800"),
            "2024-01-31 00:00:00": "2024",
            "2023-01-31 00:00:00": "2023",
            "2022-01-31 00:00:00": "2022",
            "2021-01-31 00:00:00": "2021"
        },
        width=1600,
        height=400
    )

    st.dataframe(
        csco_cash_flow_statement,
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
        intu_cash_flow_statement,
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
        sap_cash_flow_statement,
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


#Third tab contains cash flow statement information
with tab3:
    st.dataframe(
        orcl_cash_flow_statement,
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
        msft_cash_flow_statement,
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
        googl_cash_flow_statement,
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
        adbe_cash_flow_statement,
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
        crm_cash_flow_statement,
        column_config={
            "": st.column_config.Column("Salesforce", width="1800"),
            "2024-01-31 00:00:00": "2024",
            "2023-01-31 00:00:00": "2023",
            "2022-01-31 00:00:00": "2022",
            "2021-01-31 00:00:00": "2021"
        },
        width=1600,
        height=400
    )

    st.dataframe(
        csco_cash_flow_statement,
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
        intu_cash_flow_statement,
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
        sap_cash_flow_statement,
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


#Fourth tab contains fundamental ratios
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
