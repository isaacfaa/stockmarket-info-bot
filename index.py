import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from alive_progress import alive_bar; import time

def main_func():

    

    msft = yf.Ticker(str(userInput))
    with alive_bar(20, force_tty=True, spinner='arrows') as bar:
        if (msft.info['regularMarketPrice'] == None):
            print("Please input a valid Symbol")
            user_input_func()
        print(msft.info)
        bar()
        print(msft.actions)
        bar()
        print(msft.dividends)
        bar()
        print(msft.splits)
        bar()
        print(msft.financials)
        bar()
        print(msft.quarterly_financials)
        bar()
        print(msft.major_holders)
        bar()
        print(msft.institutional_holders)
        bar()
        print(msft.balance_sheet)
        bar()
        print(msft.quarterly_balance_sheet)
        bar()
        print(msft.quarterly_cashflow)
        bar()
        print(msft.earnings)
        bar()
        print(msft.quarterly_earnings)
        bar()
        print(msft.sustainability)
        bar()
        print(msft.recommendations)
        bar()
        print(msft.calendar)
        bar()
        # print(msft.earnings_dates)
        # bar()
        # print(msft.isin)
        # bar()
        # print(msft.options)
        # bar()
        print(msft.news)
        bar()
    
    download_data()

def download_data():
    ticker = yf.Ticker(str(userInput))
    data = ticker.history(str(userInputPeriod))
    data_close = data['Close']
    print(data_close)
    plt.plot(data_close)
    plt.show()

def user_input_func():
    global userInput, userInputPeriod
    print("Please input a valid Stack Name")
    print("Here are some examples: AAPL, MSFT, BA")

    userInput = input(": ")

    print("Please input period of time")
    print("Here are some examples: 5y (5 Years), 1m (1 Month)")
    userInputPeriod = input(": ")
    main_func()


user_input_func()
    
