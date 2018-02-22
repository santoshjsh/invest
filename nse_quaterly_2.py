import numpy as np
from sklearn import svm, preprocessing
import pandas as pd
import time

FEATURES=['Sales Turnover','Other Income',
          'Total Income','Total Expenses',
          'Operating profit','Gross Profit',
          'Interest','PBDT','Tax','Net Profit',
          'Earnings Per Share','Equity']

def Build_Data_Set():
    data_df=pd.read_csv('stock_quaterly_updated.csv', thousands=',')
    #store all the tickers where stock 90d days is missing
    #if 90d stock price is not available that means we need to predict stock performance
    #for those stocks
    #other way is read data directly from net 
    df=data_df[pd.isnull(data_df).any(axis=1)]
    df.to_csv('future_stock.csv')
    
    #print(len(data_df))[
    #data_df=data_df.replace('NaN',0).replace('nan',0)
    data_df.fillna(value=0,inplace=True)
    #data_df.dropna(inplace=True)
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
    return X,y,len(data_df)


def Analysis():
    test_size=50
    X,y,z=Build_Data_Set()
    clf=svm.SVC(kernel="linear", C=1.0)
    
    clf.fit(X[:-test_size],y[:-test_size])
    correct_count=0
    for x in range (1, test_size+1):
        if clf.predict(X[[-x]])[0]==y[-x]:
            correct_count+=1

    print(len(X),'Accuracy:',(correct_count/test_size)*100)        
               
               
               
Analysis()



