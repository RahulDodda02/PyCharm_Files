import requests

"""
response = requests.get("https://randomuser.me/api/")
print(response.status_code)
print(response.text)

response2 = requests.get("https://api.thedogapi.com/")
print(response2.text)


response = requests.get("https://api.thedogapi.com/v1/breeds")
response
response.request

request = response.request
request.url
request.path_url
request.method

request.headers

response
response.text
response.status_code
response.headers
"""
"""
import json
resp = requests.get('https://api.thedogapi.com/v1/breeds')
# data = json.loads(resp.read())
# price = data['quoteSummary']['result'][0]['price']['regularMarketPrice']['raw']
print(resp)
print(resp.text)

query_params = {"gender": "female", "nat": "de"}
requests.get("https://randomuser.me/api/", params=query_params).json()

"""
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}

response = requests.get(endpoint, params=query_params)
print(response)
response.json()
photos = response.json()["photos"]

print(f"Found {len(photos)} photos")
print(photos[5]["img_src"])

