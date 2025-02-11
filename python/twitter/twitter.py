import sys
import requests
from bs4 import BeautifulSoup


def get_twitter_media_urls(username):
    base_url = "https://mobile.twitter.com/"
    media_page_url = f"{base_url}{username}/media"
    media_urls = []

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
    }

    session = requests.Session()

    while True:
        response = session.get(media_page_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for tweet in soup.find_all("table", class_="tweet"):
            if tweet.find("span", class_="PlayableMedia") is not None:
                tweet_id = tweet["data-tweet-id"]
                media_url = f"https://twitter.com/{username}/status/{tweet_id}"
                media_urls.append(media_url)

        next_page = soup.find("div", class_="w-button-more")
        if next_page is None:
            break

        media_page_url = base_url + next_page.find("a")["href"]

    return media_urls


if __name__ == "__main__":
    if len(sys.argv) < 2:
        username = input("Enter your Twitter username (without @): ")
    else:
        username = sys.argv[1]

    media_urls = get_twitter_media_urls(username)
    for url in media_urls:
        print(url)
