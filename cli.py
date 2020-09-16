import click
import scrape
@click.command()
@click.option('--interval', default=30, help='Interval between scraping')
@click.option('--iterations', default=None, help='Number of Interations')

def start(interations,interval):
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