import os

import pandas

import HTMLtoCSV
import ExtractHTML

if __name__ == '__main__':
    print("Reading url file...")
    # Two dimensional array string with urls and it's name for each one
    allUrls = ExtractHTML.read_urls()
    print(f"You will extract tables from {len(allUrls)} url(s)")
    print("Starting extraction...")
    nbInvalidUrl = 0
    i = 0
    for url, name in allUrls:
        i += 1
        print(f"Url {i} on {len(allUrls)}")
        if ExtractHTML.is_url_valid(url):
            tables = ExtractHTML.get_tables(url)
            # Wikipedia pages with no tables have a len(tables) == 2
            if len(tables) > 2:
                dfs = pandas.read_html(str(tables))
                HTMLtoCSV.convert_csv(dfs, name)
        else:
            nbInvalidUrl += 1
    print(f"You extracted a total of {len(os.listdir('./output'))} table(s)")
    print(f"{nbInvalidUrl} url(s) was invalid")
    print("End of extraction, you can check the output directory :)")
