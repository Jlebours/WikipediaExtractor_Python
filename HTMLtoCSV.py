import os


def convert_csv(tables, name):
    csvname = f"{name}_"
    csvdir = './output'
    for i, table in enumerate(tables, start=1):
        fullname = os.path.join(csvdir, csvname) + f"{i}.csv"
        table.to_csv(fullname, index=False)
