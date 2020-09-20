import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import click
import analysis
import cli
#@click.command()
#@click.option('--interval', default=30, help='Interval between scraping')
#@click.option('--iterations', default=None, help='Number of Interations')


def extract_index(index_url):
    index_price=[]
    for url in index_url:
        ihtml=urlopen(url)
        isoup= BeautifulSoup(ihtml,'lxml')
        ispan=isoup.find("div", {"class" : "price-section__values"}).find("span", {"class" : "price-section__current-value"})
        if ispan.text.find(',')!=-1:
            iprice=float(ispan.text.replace(',',''))
            #djprice=float(djr)
        else:
            iprice=float(ispan.text)
        index_price.append(iprice)
    return index_price[0],index_price[1],index_price[2]

def extract_price(soup):
    span=soup.find("div", {"class" : "price-section__values"}).find("span", {"class" : "price-section__current-value"})
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
    
    
def url(df_amazon,dj,nasdaq,sp):
    

    url='https://markets.businessinsider.com/stocks/amzn-stock'
    index_url=['https://markets.businessinsider.com/index/dow_jones',
    'https://markets.businessinsider.com/index/s&p_500',
    'https://markets.businessinsider.com/index/nasdaq_100']
    
    html=urlopen(url)
    soup= BeautifulSoup(html,'lxml')
    #print(soup)
    price=extract_price(soup)
    name=extract_name(soup)
    #dp=extract_index()

  
    dp1,sp1,np1=extract_index(index_url)
    
    dj_price=analysis.price_difference(dp1,dj)
    sp_price=analysis.price_difference(sp1,sp)
    nd_price=analysis.price_difference(np1,nasdaq)
    

    if len(df_amazon)<5:
        new_data=[sp_price,nd_price,dj_price,name,str(time.ctime()),price,0]
    #return new_data
    else:
        ma=analysis.moving_average(df_amazon)
        new_data=[sp_price,nd_price,dj_price,name,str(time.ctime()),price,ma]
    

    df_amazon.loc[len(df_amazon)] = new_data
    

    return df_amazon



