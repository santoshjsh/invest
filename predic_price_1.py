import pandas as pd
import numpy as np
import time
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df=pd.read_csv('../nse_50_1.csv')
df1=df.loc[df['symbol'].isin(['ACC'])]
df1['date'] =pd.to_datetime(df.date)
df1.sort_values(by='date',inplace=True)
df1.to_csv('nse_acc_next10.csv')
df1=pd.read_csv('nse_acc_next10.csv')
df1=df1.filter(['close_price','high_price','last_traded_Price','low_price','open_price','total_traded_quantity','turnover'])
df1['label']=df1['close_price'].shift(-30)
#df1.fillna(-99999,inplace=True)



#df1.dropna(inplace=True)


#df1.drop(['label']1)
df1.drop(['close_price'], axis=1, inplace=True)
#time.sleep(3)
#df1['close_price'] = df1['close_price'].str.replace(',','')
df1['high_price'] = df1['high_price'].str.replace(',','')
df1['low_price'] = df1['low_price'].str.replace(',','')
df1['open_price'] = df1['open_price'].str.replace(',','')
df1['turnover'] = df1['turnover'].str.replace(',','')
df1['total_traded_quantity'] = df1['turnover'].str.replace(',','')

X = np.array(df1.drop(['label'],1))
X=preprocessing.scale(X)
X=X[:-30]
X_lately=X[-30:]
df1.dropna(inplace=True)
y=np.array(df1['label'].str.replace(',',''))
#df1.drop(['label'],axis=1,inplace=True)
#X_lately=np.reshape(X_lately, (10, 7))
#df1.dropna(inplace=True)
#X_lately=X_lately.reshape(len(X_lately),7)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)
clf= LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)

clf.score(X_test, y_test)
accuracy =clf.score(X_test,y_test)
print(accuracy)
forcast_set=clf.predict(X_lately)
print(forcast_set)



