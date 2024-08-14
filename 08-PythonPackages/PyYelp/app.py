import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term": "Barber",
    "location": "NYC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
print(businesses)
# print(response.text)
# to filter we can use this comprehensions, sintax: [item for item in list]
names = [business["name"]
         for business in businesses if business["rating"] > 4.5]
for business in businesses:
    print(business["name"])
