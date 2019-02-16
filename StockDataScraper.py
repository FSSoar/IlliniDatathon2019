
import requests
import json
import csv
from time import sleep

tickers = ["MMM", "BAYZF", "SYF", "HON"]
functions = ["SMA", "EMA", "MACD", "RSI", "ADX"]#, "CCI", "AROON", "BBANDS", "AD", "OBV", "WMA", "APO"



for ticker in tickers:


    dataForStock = {}
    for function in functions:

        url = "https://www.alphavantage.co/query?function=" + function +"&symbol=" + ticker + "&interval=daily&time_period=10&series_type=open&apikey=UMB1WO6HDSOV980F"

        r = requests.get(url=url)
        # array = json.loads(r.json())
        document = r.json()

        # print(document)

        # print(document['Technical Analysis: ' + function])
        # print()

        for value in document['Technical Analysis: ' + function]:
            if value not in dataForStock:
                dataForStock[value] = {"DATE" : value}
            dataForStock[value].update({function :document['Technical Analysis: ' + function][value][function]})
            # print(dataForStock[value])
            # print(value)
            # break
            
    print(len(dataForStock))
    # print(list(dataForStock["2019-02-15"].values()))

    
    with open(ticker + 'firstFive.csv', mode='w') as stockFile:
        headers = ["DATE", "SMA", "EMA", "MACD", "RSI", "ADX"]
        stockWriter = csv.DictWriter(stockFile, fieldnames=headers)
        # stockWriter.writerow(function)s
        stockWriter.writeheader()
        for value in dataForStock:
            stockWriter.writerow(dataForStock[value])



        # break
    # break
    
    sleep(60)



