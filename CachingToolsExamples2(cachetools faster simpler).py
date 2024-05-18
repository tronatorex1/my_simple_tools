# This script uses cache in order to store repeated results and avoind re-calculations of the same values. Repeated calcs are read from the cached based on size and TLL 
#   In this case, results are calculated the first time only, the second time if param are the same, cache is use and resonse time is reduced   
#      https://rawheel.medium.com/caching-method-responses-with-cachetools-in-python-b7cfd9e86ad6

from cachetools import cached, TTLCache
import time
import sys

sys.set_int_max_str_digits(maxdigits=1000000000) # sets cap for int vars

# Simple mathematical exponential calc that should take some secs to answer
@cached(cache=TTLCache(maxsize=1024, ttl=3)) # ttl: 10 segs to store the cached data, then it resets itself for another 10segs TTL
def fib() -> float:
    with open("Input_FILE.txt", "r") as f:
        res = f.readlines()

def main():
    o = time.time()
    print(f"Res = {fib()} | Elapsed: {str(float(time.time() - o))}")

if __name__ == "__main__":
    main() # my local main() version