# These are examples on how to access free public APIs with python
#   THe ones at the bottom are related to the rapidapi sire. Note that the account and Key are already in place within the code to use 

# 1 Accessing free Google's API resources
import requests
response = requests.get('https://google.com/')
print(response.text)

# this one seems not to be working any longer. Yet the example helps in understanding the possible API access structure expected
import requests
params = {"words": 10, "paragraphs": 1, "format": "json"}
response = requests.get(f"https://alexnormand-dino-ipsum.p.rapidapi.com/", params=params,
 headers={
   "X-RapidAPI-Host": "alexnormand-dino-ipsum.p.rapidapi.com",
   "X-RapidAPI-Key": "4xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"})
print (type(response.json()))
print(response.json())


# 2 Accessing rapidapi's Recipe-Food-Nutrition APIs - requires subscription
import requests
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
querystring = {"query":"pasta","cuisine":"italian","excludeCuisine":"greek","diet":"vegetarian","intolerances":"gluten","equipment":"pan","includeIngredients":"tomato,cheese","excludeIngredients":"eggs","type":"main course","instructionsRequired":"true","fillIngredients":"false","addRecipeInformation":"false","titleMatch":"Crock Pot","maxReadyTime":"20","ignorePantry":"true","sort":"calories","sortDirection":"asc","minCarbs":"10","maxCarbs":"100","minProtein":"10","maxProtein":"100","minCalories":"50","maxCalories":"800","minFat":"10","maxFat":"100","minAlcohol":"0","maxAlcohol":"100","minCaffeine":"0","maxCaffeine":"100","minCopper":"0","maxCopper":"100","minCalcium":"0","maxCalcium":"100","minCholine":"0","maxCholine":"100","minCholesterol":"0","maxCholesterol":"100","minFluoride":"0","maxFluoride":"100","minSaturatedFat":"0","maxSaturatedFat":"100","minVitaminA":"0","maxVitaminA":"100","minVitaminC":"0","maxVitaminC":"100","minVitaminD":"0","maxVitaminD":"100","minVitaminE":"0","maxVitaminE":"100","minVitaminK":"0","maxVitaminK":"100","minVitaminB1":"0","maxVitaminB1":"100","minVitaminB2":"0","maxVitaminB2":"100","minVitaminB5":"0","maxVitaminB5":"100","minVitaminB3":"0","maxVitaminB3":"100","minVitaminB6":"0","maxVitaminB6":"100","minVitaminB12":"0","maxVitaminB12":"100","minFiber":"0","maxFiber":"100","minFolate":"0","maxFolate":"100","minFolicAcid":"0","maxFolicAcid":"100","minIodine":"0","maxIodine":"100","minIron":"0","maxIron":"100","minMagnesium":"0","maxMagnesium":"100","minManganese":"0","maxManganese":"100","minPhosphorus":"0","maxPhosphorus":"100","minPotassium":"0","maxPotassium":"100","minSelenium":"0","maxSelenium":"100","minSodium":"0","maxSodium":"100","minSugar":"0","maxSugar":"100","minZinc":"0","maxZinc":"100","offset":"0","number":"10","limitLicense":"false","ranking":"2"}
headers = {
	"X-RapidAPI-Key": "84a317d396mshe2d9f8f28bfe5a0p1f3408jsn3db9d07bf281",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"}
response = requests.get(url, headers=headers, params=querystring)
print(response.json())


# 3 Rapidapi's Weather API.com - Current and future forecast
import requests
url = "https://weatherapi-com.p.rapidapi.com/current.json"
querystring = {"q":"Caracas"}
headers = {
	"X-RapidAPI-Key": "84a317d396mshe2d9f8f28bfe5a0p1f3408jsn3db9d07bf281",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
print("Location: " + response.json()['location']['name'])
print("CurrTemp: " + str(response.json()['current']['temp_c']))


import requests
url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
querystring = {"q":"Caracas","days":"2"}
headers = {
	"X-RapidAPI-Key": "84a317d396mshe2d9f8f28bfe5a0p1f3408jsn3db9d07bf281",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"}
response = requests.get(url, headers=headers, params=querystring)
print("Location: Caracas")
print("Today's max Temp C: " + str(response.json()['forecast']['forecastday'][0]['day']['maxtemp_c']))
print("Today's min Temp C: " + str(response.json()['forecast']['forecastday'][0]['day']['mintemp_c']))
print("-----------------------------------------------------")
print("Tomorrow's max Temp C: " + str(response.json()['forecast']['forecastday'][1]['day']['maxtemp_c']))
print("Tomorrow's min Temp C: " + str(response.json()['forecast']['forecastday'][1]['day']['mintemp_c']))
print("-----------------------------------------------------")