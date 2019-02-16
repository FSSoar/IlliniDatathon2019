import pandas as pd
import csv
import string

def combineCSVs():
    tickers = ["MMM", "BAYZF", "SYF", "HON"]
    for ticker in tickers:
        fileNames = [ticker + "firstFive.csv", ticker + "secondFive.csv", ticker + "thirdFive.csv"]
        element1 = pd.read_csv(fileNames[0])
        element2 = pd.read_csv(fileNames[1])
        mergeTwoFiles(element1, element2, ticker)

        element1 = pd.read_csv(ticker + "combined.csv")
        element2 = pd.read_csv(fileNames[2])
        mergeTwoFiles(element1, element2, ticker)
        


def mergeTwoFiles(element1, element2, ticker):
    common = pd.merge(element1, element2, how='left', left_on=['DATE'], right_on=['DATE']).dropna()
    common.to_csv( ticker + "combined.csv", index=False )



combineCSVs()

