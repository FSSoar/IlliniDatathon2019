from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

def getCSVData():
    ts = TimeSeries(key='VRC35Q4ME9BN01BF', output_format='csv')
    data, meta_data = ts.get_daily(symbol="BAYRY", outputsize='compact')
    pprint(data)

getCSVData()