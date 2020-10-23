# get HTML code via URL
import urllib.request  # Get HTML
from bs4 import BeautifulSoup  # Navigate in HTML


def UrltoHtml():
    req = urllib.request.urlopen("https://wikipedia.com/wiki/Comparison_between_Esperanto_and_Ido")

    myhtml = req.read()

    strhtml = myhtml.decode("utf8")

    req.close()
    #print(strhtml)  #Print html of URL
    return strhtml

def GetTables(html_doc):

    htmlparser = BeautifulSoup(html_doc, 'html.parser')
    print("-" * 40)
    tables = htmlparser.find_all('table')
    #print(soup.prettify())

    print(tables)