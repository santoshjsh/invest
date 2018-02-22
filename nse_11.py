import os
import pandas as pd
import time
#end of stock prices for each nifty fifty stock prices.
#since 01 July- 2013
#each stock would have 5 entries. '31-Mar-17','31-Mar-16','31-Mar-15','31-Mar-14','01-Jul-13'
df=pd.read_csv('../nse_50_1.csv')
df1=df.filter(['date','close_price','symbol'])

#df1.loc[df['date'].isin('31-Mar-17','01-Jul-13')]
#print(df.head())
#df.loc[df['column_name'].isin(some_values)]
df1=df1.loc[df['date'].isin(['31-Mar-17','31-Mar-16','31-Mar-15','31-Mar-14','01-Jul-13'])]
df1.to_csv('nifty50_endOfDay_stock_prices.csv')

