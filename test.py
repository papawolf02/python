import QuantLib as ql
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)

gdp = web.DataReader('GDP', 'fred', start, end)

print(gdp.ix['2013-01-01'])