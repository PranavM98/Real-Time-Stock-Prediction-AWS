import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import click
import csv
import test
import click
import scrape
import analysis
@click.command()
@click.option('--interval', default=30, help='Interval between scraping')
@click.option('--iterations', default=5, help='Number of Interations')



def start1(iterations,interval):
    #click.echo("HELLO")
    df=pd.DataFrame(columns=["S&P 50","Nasdaq","Dow-Jones","Company","DateTime","Price","Price_Difference","Moving Average"])
    dj=[]
    nasdaq=[]
    sp=[]
    p_diff=[]

    for i in range(0,int(iterations)):
        u=scrape.url(df,dj,nasdaq,sp,p_diff)
        print(u.tail(10))
        output_file=df.to_csv('Stock1.csv')
        if i>=int(iterations/2):
            test.main()
        time.sleep(int(interval))
    
    
    
    
if __name__ == "__main__":

    start1()