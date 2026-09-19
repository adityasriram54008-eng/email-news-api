import requests
from send_email import send_email

API_KEY = "9e5609838c2c482491361790dec782ab"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=9e5609838c2c482491361790dec782ab"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message = body)