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
    file = open("output/result.txt", "w")
    file.write("Results" + os.linesep)
    for i in range(len(nbtaburl)):
        a = nameurl[i]
        b = str(nbtaburl[i])
        file.write(a + " " + b + os.linesep)

    file.close()
