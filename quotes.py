import requests

response = requests.get("https://zenquotes.io/api/random")

inspiration = response.json()[0]

quote = inspiration['q']
author = inspiration['a']