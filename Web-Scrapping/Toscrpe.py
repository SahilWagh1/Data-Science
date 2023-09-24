import time
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_soup(url):
    try:
        resp = requests.get(url)
    except:
        return None
    
    if resp.status_code == 200:
        return bs(resp.text)
    else: 
        return None


def get_details(book_tag):
    try:
        title = book_tag.find('a', title=True)['title']
    except:
        title = None
    try: 
        rating = book_tag.find('p')['class'][1]
    except: 
        rating = None 
    try: 
        price = book_tag.find('p', class_='price_color').text[1:]
    except:
        price = None
    try:
        link = 'http://books.toscrape.com/catalogue/' + book_tag.find('a')['href']
    except:
        price = None
    
    ex_price = bs(requests.get(link).text).find_all('td')[2].text.strip('Â')
    
    try:
        tax =  bs(requests.get(link).text).find_all('td')[4].text.strip('Â')
    except:
        tax = None
    
    avail = bs(requests.get(link).text).find_all('td')[5].text.partition('(')[2]
    
    try:
        review = bs(requests.get(link).text).find_all('td')[6].text
    except:
        review = None
        
    return title, rating, price,ex_price,tax,avail,review,link

def get_all_books(page):
    books = []
    for i in range(1, page+1):
        url = f'http://books.toscrape.com/catalogue/page-{i}.html'
        soup = get_soup(url)
        if soup:    
            try:
                book_tags = soup.find_all('article', class_='product_pod')

                for book_tag in book_tags:
                    books.append(get_details(book_tag))
            except:
                print('error')
            time.sleep(1)

    books = pd.DataFrame(books, columns=['title', 'rating', 'price(incl.tax)','price(exl.tax)','tax','availability','review','link'])
    return books

df = get_all_books(50)
df.to_csv('toscape.csv')
