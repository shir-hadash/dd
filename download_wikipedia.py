import sys
import wikipediaapi
import requests
from bs4 import BeautifulSoup
import os

def download_wikipedia_article(title, lang="he"):
    wiki = wikipediaapi.Wikipedia(lang)
    page = wiki.page(title)
    if not page.exists():
        print("הערך לא נמצא.")
        return

    # שמירת הטקסט הראשי
    with open("article.txt", "w", encoding="utf-8") as f:
        f.write(page.text)
    print("הטקסט נשמר ל-article.txt")

    # הורדת תמונות מהערך
    url = page.fullurl
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    images = soup.find_all("img")

    os.makedirs("images", exist_ok=True)
    count = 0
    for img in images:
        src = img.get("src")
        if src and src.startswith("//upload.wikimedia.org"):
            img_url = "https:" + src
            img_data = requests.get(img_url).content
            img_name = os.path.join("images", f"image_{count}.jpg")
            with open(img_name, "wb") as handler:
                handler.write(img_data)
            print(f"הורדה: {img_url}")
            count += 1

    print(f"נמצאו והורדו {count} תמונות.")

if __name__ == "__main__":
    title = sys.argv[1] if len(sys.argv) > 1 else "תל אביב"
    lang = sys.argv[2] if len(sys.argv) > 2 else "he"
    download_wikipedia_article(title, lang)
