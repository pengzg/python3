# -*- coding:UTF-8 -*-

import requests

from bs4 import BeautifulSoup as bs

r = requests.get("https://www.cctv.com")

r.encoding = r.apparent_encoding

soup = bs(r.text)

text = soup.find_all("a")

for i in text:
    print(i.get_text())


