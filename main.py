import requests
import json
import os
from news_api import send_news

# https://newsapi.org/docs/endpoints/everything
country = "us"
category = "business"

url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=" + \
    str(os.getenv("NEWS_API_KEY"))

request = requests.get(url)
# request.json() = Dict | request.text = Str
content = request.json()

# json_obj = json.loads(content) #usable if content == string
json_fmt = json.dumps(content, indent=2)
# print(json_fmt)

# print(content)

# article["description"] is geographically restricted - Changing to Germany etc. provides the description value 
news_list = []
for article in content["articles"][:20]:
    news_dict = {}
    news_dict["Title"] = str(article["title"]).split("-")[0].strip()
    news_dict["Source"] = article["source"]["name"]
    news_dict["URL"] = article["url"]
    news_list.append(news_dict)
# print(news_list[0]["Title"])
print(news_list)

# OR 
body = ""
for article in content["articles"]:
    """If using this function = update the send_new function accordingly to STR rather than list"""
    body = body + article["title"] + "\n" + str(article["title"]).split("-")[0].strip() \
        + "\n" + article["url"] + 2*"\n"
body = body.encode("utf-8")
# print(body)

send_news(news_list)





