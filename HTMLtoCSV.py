import os


def convert_csv(tables, name):
    """
    Converts to csv the list of wikipedia tables associated with their name
    :param tables: list[DataFrame]
    :param name:str
    :return:void
    """
    csvname = f"{name}_"
    csvdir = './output'
    for i, table in enumerate(tables, start=1):
        fullname = os.path.join(csvdir, csvname) + f"{i}.csv"
        table.to_csv(fullname, index=False)
    return i


def CreateSummary(nameurl, nbtaburl):
    """
       Create the text file with the summary of the extracted tables
       output: summary.txt
       :param nameurl: list[DataFrame]
       :param nbtaburl: list[DataFrame]
    """

    file = open("output/summary.txt", "w")
    file.write("Summary of the extracted tables" + os.linesep)

    for i in range(len(nbtaburl)):
        file.write(nameurl[i] + ", " + str(nbtaburl[i]) + os.linesep)

    file.close()
