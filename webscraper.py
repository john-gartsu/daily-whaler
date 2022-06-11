"""
Web scraper script to get data about whales and climate change

"""

import requests
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
print(r.content)