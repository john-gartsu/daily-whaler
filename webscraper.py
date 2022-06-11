"""
Web scraper script to get data about whales and climate change
https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

"""

import requests
from bs4 import BeautifulSoup
import csv

# 
# url to send get request to and store in var url  
# @feature request: store url in .env file 
# store the request to url in variable r
# 
URL = "https://us.whales.org/news-blogs/news/"
r = requests.get(URL)

# 
# instantiate BeautifulSoup instance
# r.content - get raw HTML content
# html5lib - specify html parse to be used
# store html parsed
#   
soup = BeautifulSoup(r.content, 'html5lib')
# print(f'### soup: {soup} ###')
  
whale_updates=[]  # a list to store q

# find news title using <a class="pp-post-link"> 
table = soup.find('a', attrs = {'class':'pp-post-link'})
print(f'### table: {table} ###')

"""
for row in table.findAll('div',
                         attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['url'] = row.a['href']
    quote['img'] = row.img['src']
    quote['lines'] = row.img['alt'].split(" #")[0]
    quote['author'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
  
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)"""