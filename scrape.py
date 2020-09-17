import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import click
import analysis
#@click.command()
#@click.option('--interval', default=30, help='Interval between scraping')
#@click.option('--iterations', default=None, help='Number of Interations')


def extract_dj():
    dj_url='https://markets.businessinsider.com/index/dow_jones'
    dj_html=urlopen(dj_url)
    dj_soup= BeautifulSoup(dj_html,'lxml')
    dj_span=dj_soup.find("div", {"class" : "price-section__values"}).find("span", {"class" : "price-section__current-value"})
    if dj_span.text.find(',')!=-1:
        djprice=float(dj_span.text.replace(',',''))
        #djprice=float(djr)
    else:
        djprice=float(dj_span.text)
    
    return djprice

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
    
    
def url(df_amazon,dj):
    

    url='https://markets.businessinsider.com/stocks/amzn-stock'
    html=urlopen(url)
    soup= BeautifulSoup(html,'lxml')
    #print(soup)
    price=extract_price(soup)
    name=extract_name(soup)
    dp=extract_dj()
    dj_price=analysis.dowjones(dp,dj)
    print("DOW JONES", str(dj))
    
    
    if len(df_amazon)<5:
        new_data=[dj_price,name,str(time.ctime()),price,0]
    #return new_data
    else:
        ma=analysis.moving_average(df_amazon)
        new_data=[dj_price,name,str(time.ctime()),price,ma]
    
    
    
    
    df_amazon.loc[len(df_amazon)] = new_data
    #print("DATASET")
    #print(df_amazon)
    #df_amazon.append(new_data)
    return df_amazon



