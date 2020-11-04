import filecmp

import HTMLtoCSV

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Function General
    #HTMLtoCSV.createCsv_URL("https://en.wikipedia.org/wiki/Comparison_(grammar)", "Comparison_(grammar)")

    #with open("inputdata/wikiurls.txt", "r") as file:
        #for url in file:
            #wurl = "https://en.wikipedia.org/wiki/" + url
            #print(wurl)
            #HTMLtoCSV.createCsv_URL(wurl, url)

    f1="output/Comparison_(grammar)-1.csv"
    f2="output/Comparison_(grammar)-2.csv"

    print(filecmp.cmp(f1,f2))