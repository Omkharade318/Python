import requests
import json

query = input("What type of news are you interested in?\n")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-10-13&sortBy=publishedAt&apiKey=1e198d9707ff444a98f1f2968437e3ba"
'''The API key keeps on changing so dont forget to update it '''
r = requests.get(url)
news=json.loads(r.text)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("\n----------------------------------------------------------------------------------------------------\n")
    