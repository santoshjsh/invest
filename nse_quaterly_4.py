import numpy as np
from sklearn import svm, preprocessing
import pandas as pd
import time

FEATURES=['Sales Turnover','Other Income',
          'Total Income','Total Expenses',
          'Operating profit','Gross Profit',
          'Interest','PBDT','Tax','Net Profit',
          'Earnings Per Share','Equity'
          ]

def Build_Data_Set():
    data_df=pd.read_csv('stock_quaterly_updated.csv', thousands=',')
    #store all the tickers where stock 90d days is missing
    #if 90d stock price is not available that means we need to predict stock performance
    #for those stocks
    #other way is read data directly from net 
    
    
    
    #print(len(data_df))[
    #data_df=data_df.replace('NaN',0).replace('nan',0)
    #data_df.fillna(value=0,inplace=True)
    data_df.dropna(inplace=True)
    data_df=data_df.reindex(np.random.permutation(data_df.index))
    
##    print(data_df.head())
##    print(data_df.dtypes)
##    time.sleep(5)
    X=np.array(data_df[FEATURES].values)

    X=preprocessing.scale(X)
    
    y=np.array(data_df['status']
               .replace('Underperform',0)
               .replace('Outperform',1)
               .values.tolist())
    #print(len(data_df))
##    X=X.astype(int)
##    y=y.astype(int)           
    return X,y


def Analysis():
    #test_size=50
    X,y=Build_Data_Set()
    clf=svm.SVC(kernel="linear", C=1.0)
    
    clf.fit(X,y)

    data_df=pd.read_csv('future_stock.csv', thousands=',')
    Z=data_df['stock_ticker'].values.tolist()
    X=np.array(data_df[FEATURES].values)
    X=preprocessing.scale(X)
    stocks_invest=[]
    stocks_not_invest=[]
    for x in range(len(X)):
        p=clf.predict(X[[x]])[0]
        if p==1:
            stocks_invest.append(Z[x])
        else:
            stocks_not_invest.append(Z[x])

    print('invest in:', stocks_invest)
    print('Ignore these',stocks_not_invest)

    
               
               
               
Analysis()



