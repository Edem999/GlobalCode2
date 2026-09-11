# import requests

# api_key="13ebb0b656d6286c2b97a4b84d60edae"
# url = "https://api.open-meteo.com/v1/forecast?latitude=5.6037&longitude=-0.1870&current=temperature_2m%2Cweather_code"

# requests.get(url)
# reponse = requests.get(url)
# print(reponse.status_code)
# print(reponse.json())

from pprint import pprint
import requests
url = requests.get("https://api.open-meteo.com/v1/forecast?latitude=5.6037&longitude=-0.1870&current=temperature_2m%2Cweather_code")
pprint(url.json())