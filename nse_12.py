import os
import pandas as pd
import time
import datetime
#mergin all the datasets.
# 1. yearly_fin.csv+Yearly-profit-loss, yearly-ratios,nifty50_endOfDay_stock_prices

#lets first first yearly_fin + Yearly Profit Loss

df_yrlyFin=pd.read_csv('yearly_fin.csv')
df_yrlyFin.setIndex='stock_ticker'
        
              
     
df_yrlyFin=df_yrlyFin.filter(['stock_ticker', 'Year', 'Sales Turnover','Other Income',
                              'Total Income','Total Expenses','Operating profit','Gross Profit',
                              'Interest','PBDT','Net Profit','Tax','Earnings Per Share'])
#df_eoy_Stock=pd.read_csv('nifty50_endOfDay_stock_prices.csv')
df_eoy_Stock=pd.read_csv('yearly-profit-loss.csv')

#df_eoy_Stock.setIndex='stock_ticker'
#df_eoy_Stock=df_eoy_Stock.filter(['date', 'close_price', 'stock_ticker'])
#df_yrlyPl=pd.read_csv('Yearly-profit-loss.csv')
#df_yrlyRatios=pd.read_csv('yearly-ratios.csv')
merged_df=pd.merge(df_yrlyFin,df_eoy_Stock,  how='inner',on=['stock_ticker','Year'])
#merged_df.to_csv('yrlyfin_eoy.csv')

# merging yearly-ratios based on stock_ticker, Year columns
df_yrlyRatios=pd.read_csv('yearly-ratios.csv')

merged_df=pd.merge(merged_df,df_yrlyRatios,  how='inner',on=['stock_ticker','Year'])

#changing the date formate so that column Year can be used for merge condition providing composite key, (Year+stock_ticker)
merged_df.loc[merged_df.Year == "MAR'17", 'Year'] = '31-Mar-17'
merged_df.loc[merged_df.Year == "MAR'16", 'Year'] = '31-Mar-16'
merged_df.loc[merged_df.Year == "MAR'15", 'Year'] = '31-Mar-15'
merged_df.loc[merged_df.Year == "MAR'14", 'Year'] = '31-Mar-14'
merged_df.loc[merged_df.Year == "MAR'13", 'Year'] = '01-Jul-13'
merged_df.to_csv('merged_yrlyfin_pl_ratios.csv')

#because i have stock price data from 01 July 2013, i will assume EOY price for 31 Mar 13 to be same as the stock price of July 01, 2013
df_Eoy_Stock=pd.read_csv('nifty50_endOfDay_stock_prices.csv')

#changing the column name to Year in file nifty50_endOfDay_stock_prices.csv to make it consistent with merged dataset naming convention
merged_df=pd.merge(merged_df,df_Eoy_Stock,  how='inner',on=['stock_ticker','Year'])
merged_df.to_csv('merged_yrlyfin_pl_ratios_eoy.csv')
