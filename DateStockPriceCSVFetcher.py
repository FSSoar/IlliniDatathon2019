import requests
import os

def getCSVData(function, symbol):
    if function == "TIME_SERIES_DAILY" :
        url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&datatype=csv"+"&outputsize=compact"+"&apikey=UMB1WO6HDSOV980F"
    if function == "TIME_SERIES_INTRADAY":
        url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&interval=1min"+"&datatype=csv"+"&outputsize=full"+"&apikey=VRC35Q4ME9BN01BF"
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
                    file.write(chunk)
    else:
        print('File exists')

getCSVData("TIME_SERIES_INTRADAY", "MMM")
