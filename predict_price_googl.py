import pandas as pd
import quandl
import numpy as np
from sklearn import preprocessing, svm,cross_validation
from sklearn.linear_model import LinearRegression
import time
import matplotlib.pyplot as plt
from matplotlib import style

##df=quandl.get('WIKI/GOOGL')
###df.to_csv('wiki_googl_full.csv')
##
##df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
##
###df.to_csv('wiki_googl_adjstd.csv')



df=pd.read_csv('wiki_googl_adjstd.csv', index_col='Date', parse_dates=True)
##df.plot()
#df[['Adj. Open','Adj. High','Adj. Low','Adj. Close']].plot()
#plt.show()
#print('sleeping ')
#time.sleep(15)
forecast_col='Adj. Close'
#df.fillna=(-99999,inplace=True)
forecast_out=5
df['label']=df[forecast_col].shift(-forecast_out)
#df.dropna(inplace=True)
X=np.array(df.drop(['label'],1))
y=np.array(df['label'])

X=preprocessing.scale(X)
X=X[:-forecast_out]
X_lately=X[-forecast_out:]
#X=X[:-forecast_out]
df.dropna(inplace=True)
y=np.array(df['label'])

X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y, test_size=0.2)
clf=LinearRegression()
clf.fit(X_train, y_train)
accuracy=clf.score(X_test, y_test)
print(clf.predict(X_lately))
print(accuracy)




