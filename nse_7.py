import os
import pandas as pd
import time
from pathlib import Path
import shutil
from bs4 import BeautifulSoup
#loading all the files in the memory and parsing it using beautiful soap to get key financials
#problem in reading coal india.
#due to unrecognized encoding, it throws error
#we add encoding="utf8"
df=pd.read_csv('ndtv_nifty50.csv', names=['sr','link'])
df.drop('sr', axis=1, inplace=True)
df.drop(0,axis=0, inplace=True)

##stock_path=r'C:\My Program Files\Python\Python35-32\work\nse\Rediff\profit.ndtv.com\stock'
stock_path=r'C:\Program Files (x86)\Python\Python36-32\work\nse\Rediff\profit.ndtv.com\stock'

print(stock_path)
i=0

columns=[]
df1=pd.DataFrame()

try:
    for item in df['link']:
        company=item.split('/')[4]
        
        data=[]
        i=i+1
        if company!='':#'coal-india-ltd_coalindia':
            stock_index_file=Path(stock_path +'\\'+ company +'.html')   
            stock_index_dir=Path(stock_path +'\\'+ company)
            if stock_index_file.is_file() and stock_index_dir.is_dir():
                   
                print('Reading data for company '+company)
                
                f=open(str(stock_index_file),'r', encoding="utf8")
                html=f.read()
                soup=BeautifulSoup(html,"html.parser")
                table=soup.find(id='keyfunda')
                ticker=company.split('_')[1]
                data.append(ticker)
                columns.append('ticker')
                for row in table.find_all('tr'):
                    j=0
                    for td in row.find_all('td'):
                        j=j+1
                       
                        if j>1:
                           
                            data.append(td.getText())
                        if j<=1 and i==1:
                            
                            columns.append(td.getText())
                            
                if i==1:
                   df1=pd.DataFrame(data=[data],columns=columns)
                   
                else:
                   df1.loc[i]=data
                df1.to_csv('key_fin.csv')
##            if ticker=='coalindia':
##                 break
except Exception as e:
    print(str(e))
   
#        time.sleep(1)
