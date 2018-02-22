import pandas as pd
import time

#checking if the nifty 50 stocks data available to us from nse
#stock file.csv to be checked with nifty stocks.
nifty50=[
    'ACC',
'ADANIPORTS',
'AMBUJACEM',
'ASIANPAINT',
'AUROPHARMA',
'AXISBANK',
'BAJAJ-AUTO',
'BANKBARODA',
'BPCL',
'BHARTIARTL',
'INFRATEL',
'BOSCHLTD',
'CIPLA',
'COALINDIA',
'DRREDDY',
'EICHERMOT',
'GAIL',
'HCLTECH',
'HDFCBANK',
'HEROMOTOCO',
'HINDALCO',
'HINDUNILVR',
'HDFC',
'ITC',
'ICICIBANK',
'IBULHSGFIN',
'IOC',
'INDUSINDBK',
'INFY',
'KOTAKBANK',
'LT',
'LUPIN',
'M&M',
'MARUTI',
'NTPC',
'ONGC',
'POWERGRID',
'RELIANCE',
'SBIN',
'SUNPHARMA',
'TCS',
'TATAMTRDVR',
'TATAMOTORS',
'TATAPOWER',
'TATASTEEL',
'TECHM',
'ULTRACEMCO',
'VEDL',
'WIPRO',
'YESBANK',
'ZEEL'

    ]
df=pd.read_csv('stock_file_new.csv', names=['company', 'ticker'])
#df.drop(0,axis=0,inplace=True)

#df['ticker'] = map(lambda x: unicode(x).upper(), df['ticker'])
df=df.apply(lambda x: x.astype(str).str.upper())
#print(df.head())
record_found=[]
df1=pd.DataFrame()
for stock in nifty50:
    #if type(df.loc[df['ticker'] == stock])
    record_found=df.loc[df['ticker'] == stock]
    if record_found.empty:
        print('no match for', stock)
    else:
        print('match found for :-', stock)
        df3=df1.append(record_found)
    
##    if df['ticker'].where(df['ticker'] ==stock):
##        print('---yes--')
##    else:
##        print('No')
print(df3)

    #df[]
    #print(stock)
    #time.sleep(5)
#print(df.head())

