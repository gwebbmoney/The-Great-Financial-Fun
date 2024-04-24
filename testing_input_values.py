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
balance_sheet_keys_list = list(multiple_balance_sheet_statements.keys())
cash_flow_statement_keys_list = list(multiple_cash_flow_statements.keys())


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


#Desired order for balance sheet
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


#Profitability ratios
def gross_margin(income_statements):
    grossmargin = {}
    if len(income_statements) > 0:
        for keys in income_statements.keys():
            if len(keys) > 0:
                grossmargin[keys] = income_statements[keys].loc['GrossProfit']/income_statements[keys].loc['TotalRevenue']
                grossmargin[keys].index = grossmargin[keys].index.strftime('%Y')
        df1 = pd.DataFrame(grossmargin)
        df1_transpose = df1.transpose()
        return(df1_transpose)
    else:
         pass

def operating_margin(income_statements):
    operatingmargin = {}
    if len(income_statements) > 0:
        for keys in income_statements.keys():
            if len(keys) > 0:
                operatingmargin[keys] = income_statements[keys].loc['OperatingIncome']/income_statements[keys].loc['TotalRevenue']
                operatingmargin[keys].index = operatingmargin[keys].index.strftime('%Y')
        df1 = pd.DataFrame(operatingmargin)
        df1_transpose = df1.transpose()
        return(df1_transpose)

def ebitda_margin(income_statements):
    ebitdamargin = {}
    if len(income_statements) > 0:
        for keys in income_statements.keys():
            if len(keys) > 0:
                ebitdamargin[keys] = income_statements[keys].loc['EBITDA']/income_statements[keys].loc['TotalRevenue']
                ebitdamargin[keys].index = ebitdamargin[keys].index.strftime('%Y')
        df1 = pd.DataFrame(ebitdamargin)
        df1_transpose = df1.transpose()
        return(df1_transpose)

def ebit_margin(income_statements):
    ebitmargin = {}
    if len(income_statements) > 0:
        for keys in income_statements.keys():
            if len(keys) > 0:
                ebitmargin[keys] = income_statements[keys].loc['EBIT']/income_statements[keys].loc['TotalRevenue']
                ebitmargin[keys].index = ebitmargin[keys].index.strftime('%Y')
        df1 = pd.DataFrame(ebitmargin)
        df1_transpose = df1.transpose()
        return(df1_transpose)

def net_profit_margin(income_statements):
    netprofitmargin = {}
    if len(income_statements) > 0:
        for keys in income_statements.keys():
            if len(keys) > 0:
                netprofitmargin[keys] = income_statements[keys].loc['NetIncome']/income_statements[keys].loc['TotalRevenue']
                netprofitmargin[keys].index = netprofitmargin[keys].index.strftime('%Y')
        df1 = pd.DataFrame(netprofitmargin)
        df1_transpose = df1.transpose()
        return(df1_transpose)


# Calculate liquidity ratios
def working_capital_ratio(balance_sheet):
    working_capital = {}
    if len(balance_sheet) > 0:
        for keys in balance_sheet.keys():
            if len(keys) > 0:
                working_capital[keys] = balance_sheet[keys].loc['CurrentAssets']/balance_sheet[keys].loc['CurrentLiabilities']
                working_capital[keys].index = working_capital[keys].index.strftime('%Y')
        df1 = pd.DateFrame(working_capital)
        df1_transpose = df1.transpose()
        return(df1_transpose)


#Income statement information
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

    if len(keys_list) >= 3 and len(list(multiple_income_statements.keys())) >= 3:    
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

    if len(keys_list) >= 4 and len(list(multiple_income_statements.keys())) >= 4:
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

    if len(keys_list) >= 5 and len(list(multiple_income_statements.keys())) >= 5:
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

    if len(keys_list) >= 6 and len(list(multiple_income_statements.keys())) >= 6:        
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
            
    if len(keys_list) >= 7 and len(list(multiple_income_statements.keys())) >= 7:        
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
            
    if len(keys_list) >= 8 and len(list(multiple_income_statements.keys())) >= 8:        
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

#Balance Sheet Information
with tab3:
    if len(balance_sheet_keys_list) >= 1 and len(list(multiple_balance_sheet_statements.keys())) >= 1:
            if list(multiple_balance_sheet_statements.keys())[0] == balance_sheet_keys_list[0] and len(list(multiple_balance_sheet_statements.keys())) >= 1:
                st.dataframe(
                        multiple_balance_sheet_statements[balance_sheet_keys_list[0]].reindex(balance_sheet_index_order),
                        column_config={
                            "": st.column_config.Column(balance_sheet_keys_list[0], width="1800"),
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

    if len(balance_sheet_keys_list) >= 2 and len(list(multiple_balance_sheet_statements.keys())) >= 2:
            if list(multiple_balance_sheet_statements.keys())[1] == balance_sheet_keys_list[1] and len(list(multiple_balance_sheet_statements.keys())) >= 1:
                st.dataframe(
                        multiple_balance_sheet_statements[balance_sheet_keys_list[1]].reindex(balance_sheet_index_order),
                        column_config={
                            "": st.column_config.Column(balance_sheet_keys_list[1], width="1800"),
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

    if len(keys_list) >= 3 and len(list(multiple_balance_sheet_statements.keys())) >= 3:
            if list(multiple_balance_sheet_statements.keys())[2] == keys_list[2] and len(list(multiple_balance_sheet_statements.keys())) >= 1:
                st.dataframe(
                        multiple_balance_sheet_statements[keys_list[2]].reindex(balance_sheet_index_order),
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

    if len(keys_list) >= 4 and len(list(multiple_balance_sheet_statements.keys())) >= 4:
            if list(multiple_balance_sheet_statements.keys())[3] == keys_list[3] and len(list(multiple_balance_sheet_statements.keys())) >= 1:
                st.dataframe(
                        multiple_balance_sheet_statements[keys_list[3]].reindex(balance_sheet_index_order),
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

    if len(keys_list) >= 5 and len(list(multiple_balance_sheet_statements.keys())) >= 5:
            if list(multiple_balance_sheet_statements.keys())[4] == keys_list[4] and len(list(multiple_balance_sheet_statements.keys())) >= 1:
                st.dataframe(
                        multiple_balance_sheet_statements[keys_list[4]].reindex(balance_sheet_index_order),
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

    if len(keys_list) >= 6 and len(list(multiple_balance_sheet_statements.keys())) >= 6:
            if list(multiple_balance_sheet_statements.keys())[5] == keys_list[5] and len(list(multiple_balance_sheet_statements.keys())) >= 1:
                st.dataframe(
                        multiple_balance_sheet_statements[keys_list[5]].reindex(balance_sheet_index_order),
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
            
    if len(keys_list) >= 7 and len(list(multiple_balance_sheet_statements.keys())) >= 7:
            if list(multiple_balance_sheet_statements.keys())[6] == keys_list[6] and len(list(multiple_balance_sheet_statements.keys())) >= 1:
                st.dataframe(
                        multiple_balance_sheet_statements[keys_list[6]].reindex(balance_sheet_index_order),
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
            
    if len(keys_list) >= 8 and len(list(multiple_balance_sheet_statements.keys())) >= 8:
            if list(multiple_balance_sheet_statements.keys())[7] == keys_list[7] and len(list(multiple_balance_sheet_statements.keys())) >= 1:
                st.dataframe(
                        multiple_balance_sheet_statements[keys_list[7]].reindex(balance_sheet_index_order),
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


with tab4:
     if len(cash_flow_statement_keys_list) >= 1 and len(list(multiple_cash_flow_statements.keys())) >= 1:
            if list(multiple_cash_flow_statements.keys())[0] == cash_flow_statement_keys_list[0] and len(list(multiple_cash_flow_statements.keys())) >= 1:
                st.dataframe(
                        multiple_cash_flow_statements[cash_flow_statement_keys_list[0]].reindex(cash_flow_statement_index_order),
                        column_config={
                            "": st.column_config.Column(cash_flow_statement_keys_list[0], width="1800"),
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

     if len(cash_flow_statement_keys_list) >= 2 and len(list(multiple_cash_flow_statements.keys())) >= 2:
            if list(multiple_cash_flow_statements.keys())[1] == cash_flow_statement_keys_list[1] and len(list(multiple_cash_flow_statements.keys())) >= 1:
                st.dataframe(
                        multiple_cash_flow_statements[cash_flow_statement_keys_list[1]].reindex(cash_flow_statement_index_order),
                        column_config={
                            "": st.column_config.Column(cash_flow_statement_keys_list[1], width="1800"),
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

     if len(cash_flow_statement_keys_list) >= 3 and len(list(multiple_cash_flow_statements.keys())) >= 3:
            if list(multiple_cash_flow_statements.keys())[2] == cash_flow_statement_keys_list[2] and len(list(multiple_cash_flow_statements.keys())) >= 1:
                st.dataframe(
                        multiple_cash_flow_statements[cash_flow_statement_keys_list[2]].reindex(cash_flow_statement_index_order),
                        column_config={
                            "": st.column_config.Column(cash_flow_statement_keys_list[2], width="1800"),
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

     if len(cash_flow_statement_keys_list) >= 4 and len(list(multiple_cash_flow_statements.keys())) >= 4:
            if list(multiple_cash_flow_statements.keys())[3] == cash_flow_statement_keys_list[3] and len(list(multiple_cash_flow_statements.keys())) >= 1:
                st.dataframe(
                        multiple_cash_flow_statements[cash_flow_statement_keys_list[3]].reindex(cash_flow_statement_index_order),
                        column_config={
                            "": st.column_config.Column(cash_flow_statement_keys_list[3], width="1800"),
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

     if len(cash_flow_statement_keys_list) >= 5 and len(list(multiple_cash_flow_statements.keys())) >= 5:
            if list(multiple_cash_flow_statements.keys())[4] == cash_flow_statement_keys_list[4] and len(list(multiple_cash_flow_statements.keys())) >= 1:
                st.dataframe(
                        multiple_cash_flow_statements[cash_flow_statement_keys_list[4]].reindex(cash_flow_statement_index_order),
                        column_config={
                            "": st.column_config.Column(cash_flow_statement_keys_list[4], width="1800"),
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

     if len(cash_flow_statement_keys_list) >= 6 and len(list(multiple_cash_flow_statements.keys())) >= 6:
            if list(multiple_cash_flow_statements.keys())[5] == cash_flow_statement_keys_list[5] and len(list(multiple_cash_flow_statements.keys())) >= 1:
                st.dataframe(
                        multiple_cash_flow_statements[cash_flow_statement_keys_list[5]].reindex(cash_flow_statement_index_order),
                        column_config={
                            "": st.column_config.Column(cash_flow_statement_keys_list[5], width="1800"),
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

     if len(cash_flow_statement_keys_list) >= 7 and len(list(multiple_cash_flow_statements.keys())) >= 7:
            if list(multiple_cash_flow_statements.keys())[6] == cash_flow_statement_keys_list[6] and len(list(multiple_cash_flow_statements.keys())) >= 1:
                st.dataframe(
                        multiple_cash_flow_statements[cash_flow_statement_keys_list[6]].reindex(cash_flow_statement_index_order),
                        column_config={
                            "": st.column_config.Column(cash_flow_statement_keys_list[6], width="1800"),
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

     if len(cash_flow_statement_keys_list) >= 8 and len(list(multiple_cash_flow_statements.keys())) >= 8:
            if list(multiple_cash_flow_statements.keys())[7] == cash_flow_statement_keys_list[7] and len(list(multiple_cash_flow_statements.keys())) >= 1:
                st.dataframe(
                        multiple_cash_flow_statements[cash_flow_statement_keys_list[7]].reindex(cash_flow_statement_index_order),
                        column_config={
                            "": st.column_config.Column(cash_flow_statement_keys_list[7], width="1800"),
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


with tab5:
    col1, col2 = st.columns(2)
    col1.subheader("Gross Margin")
    col1.dataframe(gross_margin(multiple_income_statements))

    col2.subheader("Operating Margin")
    col2.dataframe(operating_margin(multiple_income_statements))

    col3, col4 = st.columns(2)
    col3.subheader("EBITDA Margin")
    col3.dataframe(ebitda_margin(multiple_income_statements))

    col4.subheader("EBIT Margin")
    col4.dataframe(ebit_margin(multiple_income_statements))

    col5, col6 = st.columns(2)
    col5.subheader("Net Profit Margin")
    col5.dataframe(net_profit_margin(multiple_income_statements))
