import requests
from send_email import send_email

API_KEY = "9e5609838c2c482491361790dec782ab"
topic = "tesla"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=9e5609838c2c482491361790dec782ab&"
       "language=en")

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] +"\n"+article["url"] +2*"\n"

body = "Subject: Today's news\n\n" + body
body = body.encode("utf-8")
send_email(message = body)