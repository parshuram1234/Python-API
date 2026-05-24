import json
import requests

def fetch_and_print_articles(api_url):
    response = requests.get(api_url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        
        for index, article in enumerate(articles[:2], start=5):
            print(f"Article {index}:\n {json.dumps(article, sort_keys=True, indent=4)}\n")

    else:
        print(f"Error: {response.status_code}")


api_endpoint = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=30b9665be5ba4ba49425ff666fc93fb3"
fetch_and_print_articles(api_endpoint)

"""
def jprint(obj):
    print(json.dumps(obj, sort_keys=True, indent=4))
"""