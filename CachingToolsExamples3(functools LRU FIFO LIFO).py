# This scripts shows how to use cache LRU (makes space for new res by deleting least used res)
#   Allows to query x times the exact same query, yielding: 1res = 1seg, 2-..res = 0.0Xsegs

# Import the required modules
from functools import lru_cache
import time
import requests

# Function to get the HTML Content
def get_html_data(url):
    for _ in range(10):
        response = requests.get(url)
    return response.text

# Memoized using LRU Cache
@lru_cache(maxsize=None)
def get_html_data_lru(url):
    for _ in range(10):
        response = requests.get(url)
    return response.text

# Get the time it took for a normal function
start_time = time.time()
get_html_data('https://books.toscrape.com/')
print('Time taken (normal function):', time.time() - start_time)

# Get the time it took for a memoized function (LRU cache)
start_time = time.time()
get_html_data_lru('https://books.toscrape.com/')
print('Time taken (LRU cache):      ', time.time() - start_time)