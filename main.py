import requests

API_KEY = "9e5609838c2c482491361790dec782ab"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=9e5609838c2c482491361790dec782ab"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
