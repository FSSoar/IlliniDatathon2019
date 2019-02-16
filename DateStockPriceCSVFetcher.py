import requests
import os

def getCSVData(function, symbol):
    
    url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&datatype=csv"+"&apikey=UMB1WO6HDSOV980F"
    filename = symbol + ".csv"
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

getCSVData("TIME_SERIES_DAILY", "BAYZF")