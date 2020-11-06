import os
import urllib.request as u_req
import requests
from bs4 import BeautifulSoup


def read_urls():
    BASE_WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/"
    allUrls = []
    with open("inputdata/wikiurls.txt", "r") as urls:
        for url in urls:
            finalUrl = BASE_WIKIPEDIA_URL + url
            allUrls.append([finalUrl.rstrip("\n"), url.rstrip("\n")])
    return allUrls


def get_tables(url):
    html = u_req.urlopen(url).read().decode("utf-8")
    bs = BeautifulSoup(html, 'lxml')
    tables = str(bs.find_all('table', {'class': 'wikitable'}))
    return tables


def is_url_valid(url):
    r = requests.head(f"{url}")
    return r.status_code == 200


def open_output():
    csvdir = './output'
    if not os.path.exists(csvdir):
        os.mkdir(csvdir)
