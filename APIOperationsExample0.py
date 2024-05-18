#
#
#
import requests
import json

"""GENERAL INFORMATION ON STATUSES:
200 OK: The server successfully processed the request, and the requested data is returned.
201 Created: A new resource is created on the server as a result of the request.
204 No Content: The request is successful, but there is no additional data to return.
300 Multiple Choices: The requested resource has multiple representations, each with its own URL.
302 Found (Temporary Redirect): The requested resource is temporarily located at a different URL.
304 Not Modified: The client’s cached copy of the resource is still valid, and no re-download is necessary.
400 Bad Request: The request has malformed syntax or contains invalid data, making it incomprehensible to the server.
401 Unauthorized: Authentication is required, and the client’s credentials (e.g., API key) are missing or invalid.
500 Internal Server Error: An unexpected server error occurred during request processing.
502 Bad Gateway: Acting as a gateway or proxy, the server received an invalid response from an upstream server
"""

"""-Parsing JSON
Known as deserialization, below is an example of how to convert a JSON string to a Python object.

import json
json_string = '{"name": "John Doe", "age": 30, "isEmployed": true}'
python_dict = json.loads(json_string)
print(python_dict)

-Generating JSON
Known as serialization, below is an example of how to convert a Python object to a JSON string.

python_dict = {'name': 'Jane Doe', 'age': 25, 'isEmployed': False}
json_string = json.dumps(python_dict)
print(json_string)

-Reading JSON from a File
Sometimes, you’ll want to read JSON from a file into your Python program. Below is an example of how to open a file and load JSON data using the json.load function.

with open('data.json', 'r') as file:
      data = json.load(file)

-Writing JSON to a File
In the inverse, you may also want to write JSON data to a file. Below is an example of how you can do that by using the json.dump function.

data = {'name': 'Jane Doe', 'age': 25, 'isEmployed': False}
with open('data.json', 'w') as file:
      json.dump(data, file)
"""

# Primers: first simple tests on API queries and accesses

# 1 
response = requests.get("http://api.open-notify.org/astros") 
print(response.status_code)
print(response.json()['people'])

import json 
def jprint(request_json_content): # create a formatted string of the Python JSON object, input: request.json()
    text = json.dumps(request_json_content, sort_keys=True, indent=4) 
    print(text) 

jprint(response.json())


# 2
import requests
# Replace with the desired API endpoint
url = 'https://api.example.com/books'
response = requests.get(url)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to retrieve data: {response.status_code}")


# 3
# When passing multiple values with 1 param separated with commas
url = "https://api.example.com/items?ids=123,456,789"
# In Python, you might construct this API request as follows:
item_ids = ['123', '456', '789']
params = {'ids': ','.join(item_ids)}
response = requests.get('https://api.example.com/items', params=params)


# 4
import requests
import json
# Function to get live stock data for a symbol
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
response = requests.get(url)
# Check if the response is successful
if response.status_code == 200:
    data = response.json()
    text = json.dumps(data, sort_keys=True, indent=4)
    last_refreshed = data["Meta Data"]["3. Last Refreshed"]
    price = data["Time Series (5min)"][last_refreshed]["1. open"]
    dates = data["Meta Data"]
    facts = data["Time Series (5min)"]["2024-04-01 04:00:00"]['1. open']
with open("c:/tmp/x.txt", "a+") as f:
    f.writelines(text) # saves all data contents in a file 


# 5 querying with àrams embedded into the URL (country, category and API_KEY)
import json
import requests
# Replace 'API_KEY' with your actual API key from NewsAPI
API_KEY = '3805f6bbabcb42b3a0c08a489baf603d'
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"
response = requests.get(url)
print(response.status_code)
print(response.content)
data = response.json()
articles = response.json().get('articles', []) # filters and eases the inner-data selection within the JSON variable

for i,j in enumerate(data["articles"]):
    print(f"{str(i).ljust(2)} : {j['source']['name']}")
# or
for j in articles:
    print(f"- {j['source']['name']}")

for index, article in enumerate(articles[:3], start=1):
    print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
    
with open("c:/tmp/y.txt", "w+") as f:
    f.writelines(json.dumps(data, sort_keys=True, indent=4))


# 6 Using params to pass arguments to the body (not in the URL)
import requests, json
API_URL = "https://newsapi.org/v2/top-headlines"
API_KEY = "3805f6bbabcb42b3a0c08a489baf603d"
params = {"country": "us", "apiKey": API_KEY}
# Making the API request
response = requests.get(API_URL, params=params)
if response.status_code == 200:
    text = json.dumps(response.json(), sort_keys=True, indent=4) # this creates a 'str' with formatted fields 
    type(text)
    articles = response.json().get('articles', []) # this creates a 'json' filtered variable 
    type(articles)
    for i in articles:
        print(i['author'])


# 7 requests + urllib + turtle for a more complex solution (includes graphical response)
# Python's built-in support for JSON
import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# writing results
file = open("c:/tmp/iss.txt", "w")
file.write("There are currently " + str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]
for p in people:
	file.write(p['name'] + " - on board" + "\n")



# 8 Geospatial data
# print long and lat
import geocoder
g = geocoder.ip('me')
with open("c:/tmp/iss.txt", "a+") as f:
    f.write("\nYour current lat / long is: " + str(g.latlng))
# check the contents of the iss file in a webbrowser
webbrowser.open("c:/tmp/iss.txt")

# This code has an issue: graphic files are not present, therefore, no other pics can be used as replacement
""" import turtle
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)
# load the world map image
screen.bgpic("c:/tmp/images\map.gif")
screen.register_shape("c:/tmp/images\iss.gif")
iss = turtle.Turtle()
iss.shape("c:/tmp/images\iss.gif")
iss.setheading(45)
iss.penup()
"""

## load the current status of the ISS in real-time
url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
# Extract the ISS location
location = result["iss_position"]
lat = location['latitude']
lon = location['longitude']
# Output lon and lat to the terminal in the float format
lat = float(lat)
lon = float(lon)
print("\nLatitude: " + str(lat))
print("\nLongitude: " + str(lon))


# To update the position of the ISS in the previous map that did not worked
"""
# Update the ISS location on the map
iss.goto(lon, lat)
# Refresh each 5 seconds
time.sleep(5)
"""

