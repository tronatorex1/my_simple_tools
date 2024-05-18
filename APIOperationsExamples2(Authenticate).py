# These are code examples on how to authenticate in some forms of API sites
#   These are just two types of Auth: HTTP Basic and OAUTH. There are more auth types.

# 1 HTTPBasicAuth
from requests.auth import HTTPBasicAuth
user = HTTPBasicAuth('user', 'pass')
requests.get('https://httpbin.org/basic-auth/user/pass', auth=user)
# or 
requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))


# 2 OAuth 1 Authentication
# The requests-oauthlib library allows Requests users to easily make OAuth 1 authenticated requests:
import requests
from requests_oauthlib import OAuth1
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)


# 3 Handling exceptions in the code
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=0.00001)
    # Code here will only run if the request is successful
except requests.Timeout as error:
    print(error)

try:
    response = requests.get('http://api.open-notify.org/astros.json') 
    # Code here will only run if the request is successful
except requests.ConnectionError as error:
    print(error)

# Control and Disable redirecting (errors, such as 3XX) completely within your request options:
response = requests.get('http://api.open-notify.org/astros.json', max_redirects=2)

response = requests.get('http://api.open-notify.org/astros.json', allow_redirects=False)

try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.TooManyRedirects as error:
    print(error)

# Handling various types of exceptions:
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)

