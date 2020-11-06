import os
import pandas
import HTMLtoCSV
import ExtractHTML

if __name__ == '__main__':
    print("Reading url file...")
    ExtractHTML.open_output()
    # Two dimensional array string with urls and it's name for each one
    allUrls = ExtractHTML.read_urls()
    print(f"You will extract tables from {len(allUrls)} url(s)")
    print("Starting extraction...")
    nbtaburl = []  # List of total tables created by url
    nameurl = []  # List of total url
    # counters
    nbInvalidUrl = 0
    i = 0
    k = 0
    for url, name in allUrls:
        i += 1
        print(f"Url {i} on {len(allUrls)}")
        if ExtractHTML.is_url_valid(url):
            tables = ExtractHTML.get_tables(url)
            if tables != "[]":
                try:
                    dfs = pandas.read_html(str(tables))
                except Exception as exc:
                    print("Exception type: ", exc.__class__)
                    print(f"A wikitable in the url {i} : {name} have a syntax problem, so it can't extract it")
                else:
                    nbtabs = HTMLtoCSV.convert_csv(dfs, name)  # return the number of tables
                    # The following is for the creation of the summary file
                    k += 1  # Number url that contains tables
                    nbtaburl.append(k)
                    nbtaburl[k - 1] = nbtabs
                    nameurl.append(k)
                    nameurl[k - 1] = name
        else:
            nbInvalidUrl += 1
    # Create summary of obtained tables (list url, list tables number)
    HTMLtoCSV.get_summary(nameurl, nbtaburl)
    print(f"You extracted a total of {len(os.listdir('./output'))} table(s)")
    print("You can find the summary (summary.txt) at the root of the project")
    print(f"{nbInvalidUrl} url(s) was invalid")
    print("End of extraction, you can check the output directory :)")