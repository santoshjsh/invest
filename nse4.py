import pandas as pd
import time

#navigating through all the files listed in stock_files.csv to get stock ticker

df=pd.read_csv('stock_file.csv',names=['sr','stock_path'])
df.drop('sr',axis=1,inplace=True)
df.drop(0,axis=0,inplace=True)
flist=[]
sList=df['stock_path']
stocks_list=[]
#stocks_list=[]
#print(df1)
for stock in sList[1:]:
    stock_name=stock.split('\\')[7]
    stocks_list.append(stock_name.split('_'))#[0]

df1=pd.DataFrame(stocks_list)
#refined csv file with two columns i.e. company name, ticker
df1.to_csv('stock_file_new.csv')
#print(df1.head())

