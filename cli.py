import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import click
import csv
import click
import scrape
import analysis
@click.command()
@click.option('--interval', default=30, help='Interval between scraping')
@click.option('--iterations', default=5, help='Number of Interations')



def start1(iterations,interval):
    #click.echo("HELLO")
    df_amazon=pd.DataFrame(columns=["Company","DateTime","Price","Moving Average"])

    for i in range(0,int(iterations)):
        u=scrape.url(df_amazon)
        #print(u)
        #
            
        time.sleep(int(interval))
    
    output_file=df_amazon.to_csv('Stock.csv')
    
if __name__ == "__main__":
    start1()