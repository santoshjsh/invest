import numpy as np
from sklearn import svm, preprocessing
import pandas as pd
import time

FEATURES=['Sales Turnover','Other Income',
          'Total Income','Total Expenses',
          'Operating profit','Gross Profit',
          'Interest','PBDT','Tax','Net Profit',
          'Earnings Per Share','Equity','stock_price','nifty_price'
          ]



def Build_Data_Set(industry):
    #this code can be optimized bcoz we are loading these csv files on each funcction call.
    #rather passgin dataset to this function would be better.
    
    
    data_df=pd.read_csv('stock_quaterly_updated.csv', thousands=',')
      
    data_df=data_df.loc[data_df.Industry==industry]
    
    data_df.dropna(inplace=True)
    data_df=data_df.reindex(np.random.permutation(data_df.index))
    
    X=np.array(data_df[FEATURES].values)

    X=preprocessing.scale(X)

    
    y=np.array(data_df['status']
               .replace('Underperform',0)
               .replace('Outperform',1)
               .values.tolist())
            
    return X,y


def Analysis():
    #test_size=50
    df=pd.DataFrame(columns=['industry','invest','Not Invest'])
    nifty_df=pd.read_csv('nifty/ind_nifty50list.csv', thousands=',')
    
##    time.sleep(5)
    data_df=pd.read_csv('future_stock.csv', thousands=',')
    #print(data_df.head())
    industry=pd.Series(nifty_df['Industry'])
    
    industry.drop_duplicates(inplace=True)
    
    for item in industry.iteritems():
        print(item[1])
        #time.sleep(10)
        X,y=Build_Data_Set(item[1])
        clf=svm.SVC(kernel="linear", C=1.0)
        
        clf.fit(X,y)
        stocks_invest=[]
        stocks_not_invest=[]
        #data_df=pd.read_csv('future_stock.csv', thousands=',')
        data_df=data_df.loc[data_df.Industry==item[1]]
        Z=data_df['stock_ticker'].values.tolist()
        X=np.array(data_df[FEATURES].values)
        X=preprocessing.scale(X)
        
        
        for x in range(len(X)):
            p=clf.predict(X[[x]])[0]
            if p==1:
                stocks_invest.append(Z[x])
            else:
                stocks_not_invest.append(Z[x])
        print('industry', item[1])
        print('invest in:', stocks_invest)
        print('Ignore these',stocks_not_invest)
        
        df.loc[len(df)]=[item[1],stocks_invest,stocks_not_invest]
    #print(df)
    df.to_csv('prediction.csv')
               
               
Analysis()



