import pandas as pd
import datetime
import time

df=pd.read_csv('quaterly_fin_updated.csv')

df['stock_ticker']=pd.Series(df['stock_ticker']).str.upper()

df.loc[df.Year == "JUN'17", 'Year'] = '01-Jul-17'
df.loc[df.Year == "MAR'17", 'Year'] = '01-Apr-17'
df.loc[df.Year == "DEC'16", 'Year'] = '01-Jan-17'
df.loc[df.Year == "SEP'16", 'Year'] = '01-Oct-16'
df.loc[df.Year == "JUN'16", 'Year'] = '01-Jul-16'
df.loc[df.Year == "MAR'16", 'Year'] = '01-Apr-16'
df['date']=df[['Year']]
#df.set_index=df[['date']]
df.set_index(['date'], inplace=True)
df=df[['stock_ticker','Sales Turnover','Other Income','Total Income','Total Expenses','Operating profit','Gross Profit','Interest','PBDT', 'Tax','Net Profit','Earnings Per Share','Equity']]

#Converting index column as datetime
df.index = pd.to_datetime(df.index)
#droping the duplicates as few stocks have duplicate quaterly column values on ndtv profit e.g. stocks ioc, HINDUNILVR
df.drop_duplicates(inplace=True)

df_stock=pd.read_csv('../nse_50_1.csv', index_col='date', parse_dates=True)
#df_stock.index = pd.to_datetime(df_stock.index)
df_stock=df_stock[['symbol','close_price']]

##
##df['stock_price']='NaN'
##df['stock_price_90d']='NaN'
df_nifty50=pd.read_csv('NSEI.csv', index_col='Date', parse_dates=True , usecols=['Date','Adj Close'])


for row in df.itertuples():
    
    date_90d=row.Index+pd.DateOffset(90)
    #df_stock.loc[]
    #row1=df_stock[(df_stock.index==date_90d)][['close_price','symbol']]
    stock_price_date_90d=df_stock[(df_stock.index==date_90d)&(df_stock.symbol==row.stock_ticker)]['close_price']
    stock_price_nifty50_90d=df_nifty50[(df_nifty50.index==date_90d)]['Adj Close']
    
    length=len(stock_price_date_90d)
    if length>0:
        df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'stock_price_90d'] =stock_price_date_90d[0]
        df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'nifty_price_90d'] =pd.to_numeric(stock_price_nifty50_90d)[0]
        
    else:
        #stock price for 91 days
        date_90d=row.Index+pd.DateOffset(91)
        stock_price_date_90d=df_stock[(df_stock.index==date_90d)&(df_stock.symbol==row.stock_ticker)]['close_price']
        stock_price_nifty50_90d=df_nifty50[(df_nifty50.index==date_90d)]['Adj Close']
        length=len(stock_price_date_90d)
        if length>0:
            df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'stock_price_90d'] =stock_price_date_90d[0]
            df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'nifty_price_90d'] =pd.to_numeric(stock_price_nifty50_90d)[0]
            
        else:
            #stock price for 92 days
            date_90d=row.Index+pd.DateOffset(92)
            stock_price_date_90d=df_stock[(df_stock.index==date_90d)&(df_stock.symbol==row.stock_ticker)]['close_price']
            stock_price_nifty50_90d=df_nifty50[(df_nifty50.index==date_90d)]['Adj Close']
            length=len(stock_price_date_90d)
            if length>0:
                df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'stock_price_90d'] =stock_price_date_90d[0]
                df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'nifty_price_90d'] =pd.to_numeric(stock_price_nifty50_90d)[0]
                
        
    date_d=row.Index
    stock_price_date=df_stock[(df_stock.index==date_d)&(df_stock.symbol==row.stock_ticker)]['close_price']
    stock_price_nifty50=df_nifty50[(df_nifty50.index==date_d)]['Adj Close']
    length=len(stock_price_date)
    if length>0:
        df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'stock_price'] =stock_price_date[0]#.str.replace(',','')
        df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'nifty_price'] =pd.to_numeric(stock_price_nifty50)[0]
        
    else:
        #stock price +1 day
        date_d=row.Index+pd.DateOffset(1)
        stock_price_date=df_stock[(df_stock.index==date_d)&(df_stock.symbol==row.stock_ticker)]['close_price']
        stock_price_nifty50=df_nifty50[(df_nifty50.index==date_d)]['Adj Close']
        length=len(stock_price_date)
        if length>0:
            df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'stock_price'] =stock_price_date[0]#.str.replace(',','')
            df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'nifty_price'] =pd.to_numeric(stock_price_nifty50)[0]
##            print(row.stock_ticker, stock_price_date.str.replace(',',''), 'current test1')
##            time.sleep(1)
        else:
            #stock price +2 days
            date_d=row.Index+pd.DateOffset(2)
            stock_price_date=df_stock[(df_stock.index==date_d)&(df_stock.symbol==row.stock_ticker)]['close_price']
            stock_price_nifty50=df_nifty50[(df_nifty50.index==date_d)]['Adj Close']
            length=len(stock_price_date)
            if length>0:
                df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'stock_price'] =stock_price_date[0]#.str.replace(',','')
                df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'nifty_price'] =pd.to_numeric(stock_price_nifty50)[0]
##                print(row.stock_ticker,stock_price_date.str.replace(',',''), 'current test2')
##                time.sleep(1)
##    print('----------')        
##    print(stock_price_date_90d)
    length=len(stock_price_date_90d)        
    if length>0:
        stock_diff_pc=((pd.to_numeric(stock_price_date_90d.str.replace(',',''))[0]-pd.to_numeric(stock_price_date.str.replace(',',''))[0])/pd.to_numeric(stock_price_date.str.replace(',',''))[0])*100
        nifty_diff_pc=((pd.to_numeric(stock_price_nifty50_90d)[0]-pd.to_numeric(stock_price_nifty50)[0] )/pd.to_numeric(stock_price_nifty50)[0])*100
        print('differece=', stock_diff_pc, 'nifty differ=',nifty_diff_pc )
        df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'stock_pc_change'] =stock_diff_pc
        df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'nifty_pc_change'] =nifty_diff_pc
        if stock_diff_pc>nifty_diff_pc:
            df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'status'] ='Outperform'
        else:
            df.loc[(df.index == row.Index)&(df.stock_ticker==row.stock_ticker), 'status'] ='Underperform'
##    
df.to_csv('stock_quaterly_updated.csv')

