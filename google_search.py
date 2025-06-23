import requests
from bs4 import BeautifulSoup
import json
import sys

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, "html.parser")
    results = []
    for g in soup.find_all('div', class_='tF2Cxc'):
        title = g.find('h3')
        link = g.find('a')
        if title and link:
            results.append({
                "title": title.text,
                "link": link['href']
            })
    return results

if __name__ == "__main__":
    query = sys.argv[1]
    results = google_search(query)
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
