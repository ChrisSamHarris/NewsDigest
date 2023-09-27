import requests
import json
import os
from news_api import send_news

# https://newsapi.org/docs/endpoints/everything

country = "gb"
category = "business"

url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=" + \
    str(os.getenv("NEWS_API_KEY"))

request = requests.get(url)
content = request.json()

json_fmt = json.dumps(content, indent=2)

#DEBUG
# print(json_fmt)

# article["description"] is geographically restricted - Changing to IP to Germany etc. provides the description value 
news_list = []
for article in content["articles"][:40]:
    news_dict = {}
    if article["title"] is not None:
        news_dict["Title"] = " - ".join(str(article["title"]).split(" - ")[:-1]).strip()
        # news_dict["Source"] = article["source"]["name"] # - US configuration
        news_dict["Author"] = article["author"] 
        news_dict["URL"] = article["url"]
        news_list.append(news_dict)
# print(news_list)

try:
    send_news(news_list)
except: 
    print("Failed to send email...")
    print("Have you authenticated correctly? (USR, PSSWD & API_KEY)")