import numpy as np
from sklearn import svm, preprocessing
import pandas as pd
import time




def Build_Data_Set():
    nifty_df=pd.read_csv('nifty/ind_nifty50list.csv', thousands=',')
    
    data_df=pd.read_csv('stock_quaterly_updated.csv', thousands=',')
    future_df=pd.read_csv('future_stock.csv', thousands=',')
    
    for row in nifty_df.itertuples():
        data_df.loc[(data_df.stock_ticker==row.Symbol),'Industry']=row.Industry
        future_df.loc[(future_df.stock_ticker==row.Symbol),'Industry']=row.Industry    
##    industry=pd.Series(data_df['Industry'])
##    industry.drop_duplicates(inplace=True)
    data_df.to_csv('stock_quaterly_updated.csv')
    future_df.to_csv('future_stock.csv')

    
               
               
               
Build_Data_Set()



