import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import atexit

# FUNCTIONS ############################################################

def insertPrice(price, name, currency):
    requests.get('https://octeto.000webhostapp.com/add-price.php?price={}&name={}&currency={}'.format(price, name, currency)).text

def scrapBookDepository():
    url = 'https://www.bookdepository.com/es/User-Stories-Applied-Mike-Cohn/9780321205681'
    req = requests.get(url)

    if req.status_code == 200:
        
        soup = BeautifulSoup(req.text, 'lxml')
        
        price = soup.find('span', {'class': 'sale-price'})
        
        currency = price.text.split("$")[0]
        
        price = float(price.text.split("$")[1])
        
        name = soup.find('div', {'class': 'item-info'}).h1.text

        print('200: Success {} {} {} {}'.format( datetime.now(), currency, price, name))

        name = name.replace(' ', '%20')

        insertPrice(price, name, currency)

        return {'name':name, 'price':price, 'currency':currency}

    elif req.status_code == 400:
        
        print('400: Resource not found')
        
        return {}

# SCHEDULER ############################################################

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=1)
# def interval_job():
#     scrapBookDepository()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=15)
def cron_job():
    scrapBookDepository()
    
atexit.register(lambda: sched.shutdown())

sched.start()