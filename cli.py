import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import click

import click
import scrape
@click.command()
@click.option('--interval', default=30, help='Interval between scraping')
@click.option('--iterations', default=5, help='Number of Interations')



def start1(iterations,interval):
    #click.echo("HELLO")
    if iterations is None:
        while(True):
            u=scrape.url()
            print(u)
            time.sleep(int(interval))
    else:
        for i in range(0,int(iterations)):
            u=scrape.url()
            print(u)
            time.sleep(int(interval))

if __name__ == "__main__":
    start1()