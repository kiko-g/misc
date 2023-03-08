import requests
import urllib.request
from bs4 import BeautifulSoup
from twitch_clips import clip_ids


link_css_selector = "div.gap-4:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > div:nth-child(1) > li:nth-child(1) > div:nth-child(3) > a:nth-child(1)"

# get all clips direct urls
urls = []
for clip_id in clip_ids:
    response = requests.get(f"https://clipr.xyz/{clip_id}")
    soup = BeautifulSoup(response.content, "html.parser")
    link = soup.select(link_css_selector)[0]
    url = link.get("href")
    urls.append(url)

# download urls
for url in urls:
    clipname = url.split("/")[-1]
    filename = f"data/{clipname}"
    urllib.request.urlretrieve(url, filename)
