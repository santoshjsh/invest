import pandas as pd
import time
from pathlib import Path
import shutil
#removing directories without financials
#adding all the stocks in the files stock_files.csv
sList=pd.read_csv('stocks_list.csv')
stock_path =r"C:\Program Files (x86)\Python\Python36-32\work\nse\Rediff\profit.ndtv.com\stock"
##stock_path = r"C:\My Program Files\Python\Python35-32\financials\profit.ndtv.com\stock"

#deleting all the stocks data where financials are not available
def stock_directory():
    for item in sList['Company Name']:
        full_path=stock_path+'\\'+item
        my_file = Path(stock_path+'\\'+item)
        if my_file.is_file():
            print('file is available')
            source=open(full_path,'r').read()
            print(source)
            time.sleep(1)
        else:
            
            if my_file.is_dir():
                financial_path=full_path+'\\financials'
                my_file = Path(financial_path)
                print('checking if financials exist ?', item)
                if my_file.is_file():
                    print('Opening stock', item, 'financials')
                    print('...............financials exists for ', item)
                    #source=open(full_path,'r').read()
                else:
                    #delete the folder of stock
                    print('Deleting...............'+ item)
                    #print("deleting the stock - " + item)
                    shutil.rmtree(full_path)

#saving all the file names into csv
def stock_files():
    flist=[]
    #Pathlib to iterate through the directory
    for p in Path(stock_path).iterdir():
        if p.is_file():
            #only add files path in the array variable as we have already dealt with direcotry above
            flist.append(p)

    pd.DataFrame(flist).to_csv('stock_file.csv')

stock_files()
stock_directory()
