import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as u_req
import os

url = 'https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido'
html = u_req.urlopen(url).read().decode("utf-8")
bs = BeautifulSoup(html, 'lxml')
table = str(bs.find_all('table', {'class': 'wikitable'}))
dfs = pd.read_html(table)
outname = f"Comparison_between_Esperanto_and_Ido_"
outdir = './output'
if not os.path.exists(outdir):
    os.mkdir(outdir)
i = 0
for table in dfs:
    i += 1
    fullname = os.path.join(outdir, outname) + f"{i}.csv"
    table.to_csv(fullname, index=False)
