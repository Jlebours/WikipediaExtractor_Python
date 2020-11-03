import HTMLtoCSV

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Function General
    HTMLtoCSV.createCsvURL("https://wikipedia.com/wiki/Comparison(grammar)")

    fichier = open("inputdata/wikiurls.txt")
    url = fichier.readline()
    for i in url:
        wurl = "BASE_WIKIPEDIA_URL" + i
        HTMLtoCSV.createCsvURL(wurl)