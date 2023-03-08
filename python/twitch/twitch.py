import os
import requests
import urllib.request
from bs4 import BeautifulSoup
from clips_db import clip_ids
from termcolor import colored


def get_all_clips_download_urls():
    urls = []
    link_css_selector = "div.gap-4:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > div:nth-child(1) > li:nth-child(1) > div:nth-child(3) > a:nth-child(1)"

    for i, clip_id in enumerate(clip_ids):
        index = i+1
        total = len(clip_ids)
        percentage = 100 * index / total
        print(f"\rExtracting clip download urls ({percentage:.2f}%)", end="")
        clip_url = f"https://clipr.xyz/{clip_id}"
        response = requests.get(clip_url)
        soup = BeautifulSoup(response.content, "html.parser")
        link = soup.select(link_css_selector)[0]
        url = link.get("href")
        urls.append(url)

    return urls


def download_clip(url):
    clipname = url.split("/")[-1]
    filename = f"data/{clipname}"
    urllib.request.urlretrieve(url, filename)


if __name__ == "__main__":
    urls = get_all_clips_download_urls()

    if not os.path.exists("data"):
        os.mkdir("data")

    for url in urls:
        download_clip(url)
        print(colored(f"Saved {url} to data/", "green"))
