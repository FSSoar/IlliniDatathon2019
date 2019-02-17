import requests
import os
import csv
def getCSVData(function, symbol):
    try:
        os.remove(symbol + "-" + function + ".csv")
        os.remove(symbol + "-" + function + "Testing.csv")
    except:
        pass
    if function == "TIME_SERIES_DAILY" :

        url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&datatype=csv"+"&outputsize=compact"+"&apikey=UMB1WO6HDSOV980F"
    if function == "TIME_SERIES_INTRADAY":
        url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&interval=1min"+"&datatype=csv"+"&outputsize=full"+"&apikey=VRC35Q4ME9BN01BF"
    else:
        # url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&datatype=csv&apikey=VRC35Q4ME9BN01BF"
        pass
    filename = symbol + "-" + function + ".csv"
    if not os.path.isfile(filename):
        print('Downloading File')
        response = requests.get(url)
        # Check if the response is ok (200)
        if response.status_code == 200:
            # Open file and write the content
            with open(filename, 'wb') as file:
                # A chunk of 128 bytes
                for chunk in response:
                    # print(chunk)
                    file.write(chunk)
    else:
        print('File exists')

    with open(symbol + "-" + function + ".csv", 'r') as inp, open(symbol + "-" + function + "Testing.csv", 'w') as out:
        writer = csv.writer(out)
        for row in csv.reader(inp):
            
            
            if "2018" not in row[0]:
                writer.writerow(row)
                print(row)
                # break
    print("Task Complete")

getCSVData("TIME_SERIES_DAILY", input("Put Company Ticker Symbol: "))
