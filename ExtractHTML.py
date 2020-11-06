import urllib.request as u_req
import pandas
from bs4 import BeautifulSoup


def read_urls():
    BASE_WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/"
    allUrls = []
    with open("inputdata/test.txt", "r") as urls:
        for url in urls:
            finalUrl = BASE_WIKIPEDIA_URL + url
            allUrls.append([finalUrl, url])
    return allUrls


def get_tables(url):
    html = u_req.urlopen(url).read().decode("utf-8")
    bs = BeautifulSoup(html, 'lxml')
    tables = str(bs.find_all('table', {'class': 'wikitable'}))
    dfs = pandas.read_html(tables)
    return dfs
