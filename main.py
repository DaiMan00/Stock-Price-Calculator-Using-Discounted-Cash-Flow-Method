import yfinance as yf

# Stock Intrinsic Value Calculation
stock = yf.Ticker("0001.HK")
outstandingshares = stock.info['sharesOutstanding'] # Fetch number of shares outstanding

# Assumptions:
required_rate = 0.08
perpetual_rate = 0.05
cashflowgrowthrate = 0.03

years = [1,2,3,4]

# the fresscashflow [] consists values of of free cash flow in 2017, 2018, 2019, 2020
# the values of free cash flow can be obtained from  yahoo finance -> cash flow statement -> free cash flow
# Free Cash Flow = Cash flow from Operations - Capital Expenditure

freecashflow = [1090334, 729416, 1293949, 367744] # Last 4 years, in 1000s of $

futurefreecashflow = []
discountfactor = []
discountedfuturefreecashflow = []

terminalvalue = freecashflow[-1] * (1 + perpetual_rate)/(required_rate - perpetual_rate)

print(terminalvalue)

for year in years:
   cashflow = freecashflow[-1] * (1 + cashflowgrowthrate) ** year
   futurefreecashflow.append(cashflow)
   discountfactor.append((1 + required_rate) ** year)

print(discountfactor)

print(futurefreecashflow)

for i in range(0, len(years)):
    discountedfuturefreecashflow.append(futurefreecashflow[i] / discountfactor[i])

print(discountedfuturefreecashflow)

discountedterminalvalue = terminalvalue/(1 + required_rate) ** 4
discountedfuturefreecashflow.append(discountedterminalvalue)

todaysvalue = sum(discountedfuturefreecashflow)

fairvalue = todaysvalue * 1000 / outstandingshares

print("The fair value of stock is ${}".format(round(fairvalue,2)))
