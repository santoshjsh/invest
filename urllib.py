import urllib.request
import os
with urllib.request.urlopen('https://www.equitymaster.com/stock-research/quarterly-result/infy/INFY') as response:
    html=response.read()

    
save='infy.html'
store=open(save,'w')
store.write(str(html))
store.close()
    
