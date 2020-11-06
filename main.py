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
    nbInvalidUrl = 0
    nbtaburl = []
    nameurl = []
    file = open("output/result.txt", "w")

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
                    k+=1
                    a = HTMLtoCSV.convert_csv(dfs, name)
                    #print("a= ", a)
                    print("i", i)
                    print("k", k)
                    #print(name)

                    nbtaburl.append(k)
                    nbtaburl[k - 1] = a

                    nameurl.append(k)
                    nameurl[k - 1] = name
        else:
            nbInvalidUrl += 1
    file.write("Results" + os.linesep)
    for i in range(len(nbtaburl)):

        a = nameurl[i]
        b = str(nbtaburl[i])
        file.write(a+" "+ b +os.linesep )


    file.close()
    print(f"You extracted a total of {len(os.listdir('./output'))} table(s)")

    print(f"{nbInvalidUrl} url(s) was invalid")
    print("End of extraction, you can check the output directory :)")
