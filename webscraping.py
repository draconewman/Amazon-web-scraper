# import libraries

from bs4 import BeautifulSoup 
'''Beautiful Soup is a Python library for getting data out of HTML, XML, and other markup 
languages.'''
import requests 
'''allows us to send HTTP requests using Python. The HTTP request returns a Response Object with all the 
response data (content, encoding, status, etc).'''
import time # refers to time independent of the day (hour, minute, second, microsecond)
import datetime # combines date and time information
import smtplib # to send mail to any internet machine with an SMTP or ESMTP listener daemon
import csv #Create CSV and write headers and data into the file
# import pandas as pd #for data manipulation and analysis



def check_price():
    # Connect to Website and pull in data

    URL = 'https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_1_sspa?crid=13H9W06SO874P&keywords=macbook&qid=1651348977&sprefix=macbook%2Caps%2C316&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSU9HWDVVWlVVMEpXJmVuY3J5cHRlZElkPUEwNTU4NDMzMVg0U0NQSk1RTkE3TyZlbmNyeXB0ZWRBZElkPUEwNTE5MzQ5VkNMSVBKNDZPQ0w3JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    URL2 = 'https://www.amazon.in/Dell-XPS-9305-i7-1165G7-ICC-C786501WIN8/dp/B09NLR3MMF/ref=sr_1_1_sspa?crid=2Y24VMBA495EN&keywords=dell+laptop&qid=1653673888&refinements=p_n_feature_thirteen_browse-bin%3A12598163031&rnid=12598141031&s=computers&sprefix=dell+lapto%2Caps%2C328&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUVowMVhGWFBDN0hRJmVuY3J5cHRlZElkPUEwODE4ODU2M1Q3S0tRSTNUMzRHOCZlbmNyeXB0ZWRBZElkPUEwNjgwMzE2MlZUNDdRSk1aTzZSTCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
    URL3 = 'https://www.amazon.in/dp/B09WRG7HDV/ref=s9_acsd_al_bw_c2_x_2_t?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=SVM1R2FY5ZV1SZWENDZY&pf_rd_t=101&pf_rd_p=20250f57-8c2c-4ab5-8114-fa74dac154d3&pf_rd_i=3474656031'
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    
    page = requests.get(URL3, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    # print(soup2)
    title = soup2.find(id='productTitle').get_text().strip()
    # print(title)
    # price = soup2.find(id='_price').get_text()
    # print(price)
    price = int(float(soup2.find('span', attrs = {'class' : "a-offscreen"}).get_text().strip().replace(',', '')[1:]))
    # print(price)

    today = datetime.date.today()
    # print(today)

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]


    # Now we are appending data to the csv

    with open('Dataset2.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        # writer.writerow(header) 
        writer.writerow(data)
    
    # import pandas as pd
    # df = pd.read_csv(r'C:\Users\acer\Dataset2.csv')
    # # print(df)


# Runs check_price after a set time and inputs data into our CSV

while(True):
    check_price()
    time.sleep(5) # per day

# check_price() 
