import os
import urllib.request as u_req
import requests
from bs4 import BeautifulSoup


def read_urls():
    """
    Returns the complete and valid url of the wikipedia page associated with the page name
    :return:list[list[str]]
    """
    BASE_WIKIPEDIA_URL = "https://en.wikipedia.org/wiki/"
    allUrls = []
    with open("inputdata/wikiurls.txt", "r") as urls:
        for url in urls:
            finalUrl = BASE_WIKIPEDIA_URL + url
            allUrls.append([finalUrl.rstrip("\n"), url.rstrip("\n")])
    return allUrls


def get_tables(url):
    """
    Retrieves all the tables that from the url data that have as class "wikitable" in html
    :param url:str
    :return tables:str
    """
    html = u_req.urlopen(url).read().decode("utf-8")
    bs = BeautifulSoup(html, 'lxml')
    for table in (bs.find_all('table', {'class': 'navbox mw-collapsible autocollapse'})):
        table.decompose()

    tables = str(bs.find_all('table', {'class': 'wikitable'}))
    return tables


def is_url_valid(url):
    """
    Returns true if the wikipedia page of the url is valid
    :param url:str
    :return:bool
    """
    r = requests.head(f"{url}")
    return r.status_code == 200


def open_output():
    """
    Opens an output directory so that csv's can be saved there if it does not already exist.
    :return:void
    """
    csvdir = 'output'
    if not os.path.exists(csvdir):
        os.mkdir(csvdir)
    csvdir = 'output/python'
    if not os.path.exists(csvdir):
        os.mkdir(csvdir)
