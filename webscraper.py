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

# an empty list to store whale data to WRITE to 
whale_data_list=[] 

# find news title using <div class="pp-content-grid-inner pp-content-body clearfix"> 
table = soup.find('div', attrs = {'class':'pp-content-grid-inner pp-content-body clearfix'})
# print(f'### table: {table} ###')

# span = soup.find("span", attrs= {"class":"pp-content-post-author"})
# print(span)


# to do:
# need to iterate over table var and parse span for author && date updated

for row in table.findAll('div', attrs = {'class':'pp-content-post-data'},:
    # print(row)
    # create initial whale data dict
    whale_data_dict = {}
    # need way to get title
    whale_data_dict['title'] = row.h3.text
    # print(whale_data_dict['title'])

    # author
    # span = soup.find("span", attrs= {"class":"pp-content-post-author"})
#    print(span)

    # whale_data_dict['author'] = row.span.
    print(row.span)
    
    # example
    # quote = {}
    # quote['theme'] = row.h5.text
    # quote['url'] = row.a['href']
    # quote['img'] = row.img['src']
    # quote['lines'] = row.img['alt'].split(" #")[0]
    # quote['author'] = row.img['alt'].split(" #")[1]
    # quotes.append(quote)


"""

filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','url','img','lines','author'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)
    
"""