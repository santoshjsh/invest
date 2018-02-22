import urllib
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
#extracting  all the nifty fifty stocks on money.rediff. to pull data for only these 50 stocks.
##link='http://money.rediff.com/indices/nse/nifty-50'
##
##source=urllib.request.urlopen(link).read()
##soup=BeautifulSoup(source,"html.parser")
##table=soup.find('table')
##stock_link=[]
##df=pd.DataFrame()
##thefile = open('text.txt', 'w')
###print(table)
##for row in table.find_all('tr')[1:]:
##    for link in row.find_all('a'):
##        href=link.get('href')
##        stock_link.append(href)
##    
##    
##df = pd.DataFrame({'links':stock_link})
##df.to_csv('rediff_nifty50.csv')

#-------------
#fresh appraoch as money.rediff has a different pattern of loading individual stock pattern
#like the above nifty 50 page has links in this format http://money.rediff.com/companies/acc/11510001,
#while it redirects at http://money.rediff.com/companies/Acc-Ltd/11510001 for loading Acc

# we need all the links with right href resources to be able to pull the data.
#we use ndtv profit.

link='http://profit.ndtv.com/market/domestic-index-nse_nifty/constituents'

source=urllib.request.urlopen(link).read()
soup=BeautifulSoup(source,"html.parser")
peerlist2=soup.find(id='peerlist2')
stock_link=[]
df=pd.DataFrame()

#print(table)
for link in peerlist2.find_all('a'):
    href=link.get('href')
    stock_link.append(href)
    
    
df = pd.DataFrame({'links':stock_link})
df.to_csv('ndtv_nifty50.csv')
