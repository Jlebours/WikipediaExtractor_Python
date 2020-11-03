import HTMLtoCSV

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Function General
    HTMLtoCSV.createCsv_URL("https://en.wikipedia.org/wiki/Comparison_(grammar)")

    with open("inputdata/wikiurls.txt", "r") as file:
        for url in file:
            wurl = "https://wikipedia.com/wiki/" + url
            print(wurl)
            HTMLtoCSV.createCsv_URL(wurl)