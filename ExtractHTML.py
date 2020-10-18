# get HTML code via URL
import urllib.request

def UrltoHtml():
    req = urllib.request.urlopen("https://wikipedia.com/wiki/Comparison_between_Esperanto_and_Ido")

    myhtml = req.read()

    strhtml = myhtml.decode("utf8")

    req.close()
    print(strhtml)  #Print html of URL

