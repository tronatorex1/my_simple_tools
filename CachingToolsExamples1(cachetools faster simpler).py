# This scripts use cache in order to store repeated results and avoind re-calculations of the same values. Repeated calcs are read from the cached based on size and TLL 
#   In this case, results are calculated the first time only, the second time if param are the same, cache is use and resonse time is reduced   
#      https://rawheel.medium.com/caching-method-responses-with-cachetools-in-python-b7cfd9e86ad6

from cachetools import cached, TTLCache
import time
import sys

sys.set_int_max_str_digits(maxdigits=1000000000) # sets cap for int vars

# Simple mathematical exponential calc that should take some secs to answer
@cached(cache=TTLCache(maxsize=1024, ttl=3)) # ttl: 10 segs to store the cached data, then it resets itself for another 10segs TTL
def fib(n) -> float:
    res = 0 
    for i in range(n):
        res1 = (i ** 2 ** 2) # this formula allows to create a number that takes a coupl to seconds to calc
    for j in range(n):
        res2 = (j ** 3 ** 2) # this formula allows to create a number that takes a coupl to seconds to calc
    return res1, res2 

def main():
    o = time.time()
    print(f"Res = {fib(1215)} | Elapsed: {str(float(time.time() - o))}")

if __name__ == "__main__":
    main() # my local main() version