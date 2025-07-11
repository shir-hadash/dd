import sys
import requests
from urllib.parse import quote

def download_wikipedia_pdf(title, lang="he"):
    title_encoded = quote(title.replace(" ", "_"))
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/pdf/{title_encoded}"

    headers = {
        "User-Agent": "github-actions-bot/1.0 (https://github.com/shir-hadash/dd)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("הערך לא נמצא או שגיאה בהורדה.")
        return

    with open("article.pdf", "wb") as f:
        f.write(response.content)
    print("הקובץ article.pdf נשמר בהצלחה.")

if __name__ == "__main__":
    title = sys.argv[1] if len(sys.argv) > 1 else "תל אביב"
    lang = sys.argv[2] if len(sys.argv) > 2 else "he"
    download_wikipedia_pdf(title, lang)
