import os
import pandas as pd
import time
from pathlib import Path
import shutil
from bs4 import BeautifulSoup
#building on nse_8 
#reading financials-historical-profit-loss
#adds ticker at the begining of dataset
#47 stocks pulled, and read.
#18 columns 5 rows each stock data. as the data starts from 2013(5 years)

df=pd.read_csv('ndtv_nifty50.csv', names=['sr','link'])
df.drop('sr', axis=1, inplace=True)
df.drop(0,axis=0, inplace=True)

stock_path=r'C:\My Program Files\Python\Python35-32\work\nse\Rediff\profit.ndtv.com\stock'

print(stock_path)
i=0

#columns=['ticker']
df1=pd.DataFrame()
df2=pd.DataFrame()
df3=pd.DataFrame()
result_df=pd.DataFrame()

try:
    for item in df['link']:
        company=item.split('/')[4]
        
        df1=pd.DataFrame()
        data=[]
        i=i+1
        st_ticker=[]
        
        if company!='':#'coal-india-ltd_coalindia':
            stock_index_file=Path(stock_path +'\\'+ company)
                                  #reading files under directory
            stock_index_file_in=Path(stock_path +'\\'+ company +'\\financials-historical-profit-loss')
            stock_index_dir=Path(stock_path +'\\'+ company )
            if stock_index_file_in.is_file() and stock_index_dir.is_dir():
                   
                print('Reading data for company '+company)
                
                f=open(str(stock_index_file_in),'r', encoding="utf8")
                html=f.read()
                soup=BeautifulSoup(html,"html.parser")
                table=soup.find(id='profitLoss')
                #print(table)
                #time.sleep(100)
                #columns.append('ticker')
                ticker=company.split('_')[1]
                #ticker column data
                
                count=0
                #columns.append('yearly_date')
                for row in table.find_all('tr'):
                   #print(row)
                    j=0
                    col_1=''
                    col_2=''
                    col_3=''
                    col_4=''
                    col_5=''
                    col_6=''
                    #data.append(ticker)
                    #------ reading th data from the table.
##                    print("reading column no: ",j)
                    row_head=[]
                    for th in row.find_all('th'):
                        j=j+1
                        
                        if j==1: #and i==1:
                            #print('first row first column')
                            col_1='Year' #str(th.getText())
                            
                        elif j==2:
                            col_2=str(th.getText()).split("\n")[0]
                            
                            #print(col_2)
                            #columns.append(col_2)
                            #break
                        elif j==3:
                            col_3=str(th.getText()).split("\n")[0]
                            
                            #print(col_3)
                           # columns.append(col_3)
                            #break
                        elif j==4:
                            col_4=str(th.getText()).split("\n")[0]
                            
                            #print(col_4)
                            #columns.append(col_4)
                            #break
                        elif j==5:
                            col_5=str(th.getText()).split("\n")[0]
                            
                           # print(col_5)
                            #columns.append(col_5)
                            #break
                        else :
                            col_6=str(th.getText()).split("\n")[0]
                            
##                    
##                    
##                    #row_head.append(col_1)
##                    row_head.append(col_2)
##                    row_head.append(col_3)
##                    row_head.append(col_4)
##                    row_head.append(col_5)
##                    row_head.append(col_6)
##                    
##                    
##                    series_head=pd.Series()
##                    series_head=pd.Series(row_head,name=col_1)
                    #print(series_head)
                      
                    
                    #------ reading td data from the table.
                  
                    row_data=[]
                    j=0
                    for td in row.find_all('td'):
                        j=j+1
                        #print(td.getText(),j)
##                        time.sleep(2)
                        if j==1: #and i==1:
                            col_1=str(td.getText()).strip()
                            #columns.append(col_1)
                            #print(col_1, j)
                            #time.sleep(2)
                        if j==2:
                            col_2=str(td.getText()).strip()
                            
##                            row_data.append(col_2)
                            #print(col_2)
                            #columns.append(col_2)
                            #break
                        elif j==3:
                            col_3=str(td.getText()).strip()
                            
##                            row_data.append(col_3)
                            #print(col_3)
                           # columns.append(col_3)
                            #break
                        elif j==4:
                            col_4=str(td.getText()).strip()
                            
                            #row_data.append(col_4)
##                            #print(col_4)
                            #columns.append(col_4)
                            #break
                        elif j==5:
                            col_5=str(td.getText()).strip()
                            
##                            row_data.append(col_5)
                           # print(col_5)
                            #columns.append(col_5)
                            #break
                        else :
                            col_6=str(td.getText()).strip()
                            
##                            row_data.append(col_6)
                           # print(col_6)
                            #columns.append(col_6)
                            #break
                    #print(j)
                    #row_data.append(ticker)
                    
                    row_data.append(col_2)
                    row_data.append(col_3)
                    row_data.append(col_4)
                    row_data.append(col_5)
                    row_data.append(col_6)
                    #if len(df1)>0:
                    #print('existing DF', df1.shape)
                    #df1[col_1]=pd.DataFrame(row_data)
                    
                    #df1[col_1]=pd.DataFrame(row_data,index=pd.Series(range(1,6)))
                    #df2 = pd.DataFrame(row_data, index=pd.Series(range(1,6), name='reliance'), columns=["Fin_Col{}".format(i) for i in range(1,19)])
                    tr_total=table.find_all('tr')
                   # counts=len(tr_total)-1
                    
##                    print(counts)
##                    for count in counts:
                    #print('row',row_data, 'len row data', len(row_data))
                    #time.sleep(5)
                    if count<5:
                        st_ticker.append(ticker)
                       
                    series_row=pd.Series()
                    if len(row_data)==5:
                        print('columns',col_1)
                        series_row=pd.Series(row_data,name=col_1)
                        
                        #or below
                        #df2 = pd.DataFrame(row_data, index=pd.Series(range(1,7), name='sr'), columns=[col_1])
                        
                        if count!=len(tr_total):
                            #print('row-column', count)
                            
                            df1=pd.concat([df1,series_row],axis=1)
                            #time.sleep(1)
                    
                    if count==len(tr_total)-1:
                        print('---------New Dataset result_df is ready', count, ticker,len(tr_total))
                        #df3=pd.concat([df1,df3],axis=0)
                        
                        series_ticker=pd.Series(st_ticker,name='stock_ticker')
                        df1=pd.concat([series_ticker,df1],axis=1)
                        new_df1=df1.filter(['stock_ticker','Year','Net Sales','Employee Cost','Total Expenditure',
                                            'Equity Dividend (%)',
                                            'Book Value (in ₹)'],axis=1)
                        
                        print('---------New Dataset filtered  is ready')
                        #time.sleep(2)
                        result_df = pd.concat([result_df,new_df1],axis=0)
##                           # break;
##                            else
##                                df2 = pd.DataFrame(row_data, index=pd.Series(range(1,7), name='sr'), columns=[col_1])
##                                df1=pd.concat([df1,df2],axis=0)
                    count=count+1
                    print('*****final loop count', count)                
##                    else:
##                        df1=pd.DataFrame(columns=[col_1])
##                        df1[]
                    #break;
                   # print(row_data)
        #result_df=pd.concat(series_head,result_df,axis=1)
       # time.sleep(1)
    result_df.to_csv('yearly-profit-loss.csv')
except Exception as e:
    print(str(e))
   
#        time.sleep(1)
