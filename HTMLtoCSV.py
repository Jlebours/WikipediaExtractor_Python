import os

def convert_csv(tables, name):
    """
    Converts to csv the list of wikipedia tables associated with their name
    :param tables: list[DataFrame]
    :param name:str
    :return:int
    """
    csvname = f"{name}_"
    csvdir = './output'
    nbtable = 0
    for table in tables:
        nbtable += 1
        fullname = os.path.join(csvdir, csvname) + f"{nbtable}.csv"
        table.to_csv(fullname, index=False)
    return nbtable


def get_summary(nameurl, nbtaburl):
    """
    Create the text file summary.txt which summarise the extraction at the root of the project
    :param nameurl: list[DataFrame]
    :param nbtaburl: list[DataFrame]
    :return:void
    """
    file = open("summary.txt", "w")
    file.write("Summary of the extracted tables" + os.linesep)
    for i in range(len(nbtaburl)):
        file.write(nameurl[i] + ", " + str(nbtaburl[i]) + os.linesep)
    file.close()
