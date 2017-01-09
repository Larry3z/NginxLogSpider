#!/usr/bin/env python
# coding=utf-8

from random import choice

import requests
from bs4 import BeautifulSoup

from browser import *


def get_product_urls():
    product_urls = []
    headers = {"User-Agent": choice(user_agent)}
    resp = requests.get(nginx_url, headers=headers, timeout=1)
    content = resp.content
    soup = BeautifulSoup(content, "html.parser")
    links = soup.select('a[href^="/product"]')
    for link in links:
        url = nginx_url + link.get("href")
        product_urls.append(url)
    return product_urls


def main():
    urls = get_product_urls()
    for url in urls:
        print url


if __name__ == "__main__":
    main()
