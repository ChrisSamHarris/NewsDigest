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
# request.json() = Dict | request.text = Str
content = request.json()

# json_obj = json.loads(content) #usable if content == string
json_fmt = json.dumps(content, indent=2)

#DEBUG
print(json_fmt)
# print(content)

# article["description"] is geographically restricted - Changing to Germany etc. provides the description value 
news_list = []
for article in content["articles"][:40]:
    news_dict = {}
    if article["title"] is not None:
        news_dict["Title"] = str(article["title"]).split("-")[0].strip()
        # news_dict["Source"] = article["source"]["name"] # - US configuration
        news_dict["Author"] = article["author"] 
        news_dict["URL"] = article["url"]
        news_list.append(news_dict)
# print(news_list[0]["Title"])
# print(news_list)

try:
    send_news(news_list)
except: 
    print("Failed to send email...")
    print("Have you authenticated correctly?")

#### OR ####

# body = ""
# for article in content["articles"]:
#     """If using this function = update the send_new function accordingly to STR rather than list"""
#     body = body + str(article["title"]) + "\n" + str(article["title"]).split("-")[0].strip() \
#         + "\n" + str(article["url"]) + 2*"\n"
# body = body.encode("utf-8")
# print(body)