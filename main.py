import HTMLtoCSV

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Function General
    HTMLtoCSV.createCsv_URL("https://en.wikipedia.org/wiki/Comparison_(grammar)", "Comparison_(grammar)")
    HTMLtoCSV.createCsv_URL("https://en.wikipedia.org/wiki/Comparison_between_Ido_and_Interlingua",
                            "Comparison_between_Ido_and_Interlingua")
    HTMLtoCSV.createCsv_URL("https://en.wikipedia.org/wiki/Comparison_between_Esperanto_and_Ido",
                            "Comparison_between_Esperanto_and_Ido")

    #with open("inputdata/wikiurls.txt", "r") as file:
        #for url in file:
            #wurl = "https://en.wikipedia.org/wiki/" + url
            #print(wurl)
            #HTMLtoCSV.createCsv_URL(wurl, url)
