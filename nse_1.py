import os
import pandas as pd
import time
#Reading all the stock tickers from the directory profit.ndtv.com
stock_path = r"C:\Program Files (x86)\Python\Python36-32\work\nse\Rediff\profit.ndtv.com\stock"
##stock_path = r"C:\Users\kdqv0796\Downloads\financials\profit.ndtv.com\stock"
stocks_list=[]
stock_list=[x[0] for x in os.walk(stock_path)]
#pd.DataFrame(stock_list).to_csv('test')
for each_dir in stock_list[1:]:
    stocks_list.append(each_dir.split("\\")[9])
    #time.sleep(5)

df=pd.DataFrame(stocks_list).drop_duplicates()
df.to_csv('stocks_list.csv')


sList=pd.read_csv('stocks_list.csv', names=['number','Company Name'])
#drop column number
sList.drop('number', axis=1, inplace=True)
#drop frist row
sList.drop(0, axis=0, inplace=True)
sList.to_csv('stocks_list.csv')



##for stock in sList[0]:
##    print(stock)
##    time.sleep(5)

    


