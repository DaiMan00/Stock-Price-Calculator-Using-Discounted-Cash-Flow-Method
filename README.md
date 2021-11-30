# Module needed to be installed using pip:
yfinance

# Introduction
This python script uses the disctounted cash flow method to calculate the intrinsic value of a particular stock. As there is a possibility that Yahoo Finance may be posting financial data with error, the figures of Free Cash Flow in 4 different FYs have to be inputed manually. This has provided the room for the user to double check with the actual fiugures in the financial reports, while calculting the stock price using the DCF method without needing to crunch numbers on Excel in a faster way.

The perpectual rate, required rate and cash flow growth rate are to be set by the user.

# Example: Check the figures of Free Cash Flow (Stock Quote: AMD)
website: https://finance.yahoo.com/quote/AMD/cash-flow?p=AMD
Financials -> Cash Flow -> Annual(Choose) -> Free Cash Flow of 4 FYs
