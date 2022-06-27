import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from alive_progress import alive_bar; import time

def main_func():
    msft = yf.Ticker(str(userInput))
    with alive_bar(7, force_tty=True, spinner='arrows') as bar:
        print(msft.financials)
        bar()
        print(msft.major_holders)
        bar()
        print(msft.institutional_holders)
        bar()
        print(msft.balance_sheet)
        bar()
        print(msft.quarterly_cashflow)
        bar()
        print(msft.earnings)
        bar()
        print(msft.sustainability)
        bar()
    print("Would you like to see the stock history and the latest closing price? (y/n)")
    ask_user = input(": ")
    if str(ask_user) == "y" or "Y":
        download_data()
    elif str(ask_user) == "n" or "N":
        exit()
    else:
        print("We'll take that as a no :)")


def verification():
    msft = yf.Ticker(str(userInput))
    if (msft.info['regularMarketPrice'] == None):
            print("Please input a valid Symbol")
            user_input_func()
    elif (str(userInputPeriod) == "1d"):
            print("Please input a valid period")
            user_input_func()
    else:
        main_func()
        

def download_data():
    ticker = yf.Ticker(str(userInput))
    data = ticker.history(str(userInputPeriod))
    data_latest = ticker.history(period='1d')['Close'][0]
    data_latest_2dp = "{:.2f}".format(data_latest)
    data_close = data['Close']
    print(data_close)
    plt.title("Latest Closing Price for " + str(userInput) + " is: " + "$" + str(data_latest_2dp))
    plt.plot(data_close)
    plt.show()

def user_input_func():
    global userInput, userInputPeriod
    print("Please input a valid Stack Name")
    print("Here are some examples: AAPL, MSFT, BA")

    userInput = input(": ")

    print("Please input period of time (Must be longer than 1 day)")
    print("Here are some examples: 5y (5 Years), 1m (1 Month)")
    userInputPeriod = input(": ")
    verification()


user_input_func()
    
