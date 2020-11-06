import OLD_HTMLtoCSV

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Function General
    # OLD_HTMLtoCSV.createCsvURL("https://wikipedia.com/wiki/Comparison(grammar)")
    # OLD_HTMLtoCSV.createCsv_URL("https://wikipedia.com/wiki/Comparison(grammar)")

    with open("inputdata/wikiurls.txt", "r") as file:
        for url in file:
            wurl = "https://wikipedia.com/wiki/" + url
            print(wurl)
            OLD_HTMLtoCSV.createCsv_URL(wurl)
