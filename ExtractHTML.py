# get HTML code via URL
# Implementation references : thepythoncode.com/article/convert-html-tables-into-csv-files-in-python
import urllib.request as u_req
import pandas
import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"


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


def urlToHtml(url):
    """Get the soup using the HTML content of `url` """
    # initialize a session
    session = requests.Session()
    # set the User-Agent as a regular browser
    session.headers['User-Agent'] = USER_AGENT
    # request for english content (optional)
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    # make the request
    html = session.get(url)
    # return the soup
    return BeautifulSoup(html.content, "html.parser")


def get_All_Tables(soup):
    """ Get all tables content of `url` """
    tables = soup.find_all('table', {'class': 'wikitable'})
    # print(tables)
    return tables


# old method of get_headers()
def get_Table_Headers(table):
    """ Get all headers for table content of `url` """
    headers = []
    for th in table.find("tr").find_all("th"):
        headers.append(th.text.strip())
    return headers


# old method of get_rows()
def get_Table_Rows(table):
    """ Get all row for table content of `url` """
    rows = []
    for tr in table.find_all("tr")[1:]:
        print(tr.find_all)
        cells = []
        # grab all td tags in this table row
        tds = tr.find_all("td")
        if len(tds) == 0:
            # if no td tags, search for th tags
            # can be found especially in wikipedia tables below the table
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            # use regular td tags
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)
    return rows


def get_headers(table):
    headers = []
    for column in table.find("tr").find_all(['td', 'th']):
        headers.append(column.text.strip())
    return headers


def get_rows(table):
    rows = []
    for row in table.find_all('tr')[1:]:
        rows.append([val.text.strip() for val in row.find_all(['td', 'th'])])
    return rows
