import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import click

@click.command()
@click.option('--interval', default=30, help='Interval between scraping')
@click.option('--iterations', default=None, help='Number of Interations')


def extract_price(soup):
    #Extract Price
    results = soup.find("div", {"class" : "price-section__values"})
    span=results.find("span", {"class" : "price-section__current-value"})
    #Price has , in it
    if span.text.find(',')!=-1:
            res=float(span.text.replace(',',''))
            price=float(res)
    else:
        price=float(span.text)
        
    return price
    
def extract_name(soup):
    results1 = soup.find("div", {"class": "price-section__row"})
    span1=results1.find("span", {"class":"price-section__label"})
    name=span1.text
    
    return name
    
    
def url(df_amazon):


    url='https://markets.businessinsider.com/stocks/amzn-stock'
    html=urlopen(url)
    soup= BeautifulSoup(html,'lxml')
    #print(soup)
    price=extract_price(soup)
    name=extract_name(soup)
    #Extract CompanyName
   
    new_data=[name,str(time.ctime()),price]
    #return new_data      
    df_amazon.loc[len(df_amazon)] = new_data
    #df_amazon.append(new_data)
    return df_amazon



def start(interations,interval):
    click.echo("IN")
    df_amazon=pd.DataFrame(columns=["Company","DateTime","Price"])
    if iterations is None:
        while(True):
            u=url(df_amazon)
            print(u)
            time.sleep(int(interval))
    else:
        for i in range(0,int(iterations)):
            u=url(df_amazon)
            print(u)
            time.sleep(int(interval))

