import pandas
import ExtractHTML
import os

def save_As_Csv(table_name, headers, rows):
    """HTML to CSV for table content of `url` """
    pandas.DataFrame(rows, columns=headers).to_csv("./output", f"{table_name}.csv", index=False)


# All tables of a URL
def createCsv_URL(wurl, url):
    if not (os.path.exists("./output")):
        # define the name of the directory to be created
        path = "./output"
        # define the access rights
        access_rights = 0o777
        try:
            os.mkdir(path, access_rights)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s" % path)
    soup = ExtractHTML.urlToHtml(wurl)
    tables = ExtractHTML.get_All_Tables(soup)
    print(f"[+] Found a total of {len(tables)} tables.")
    # iterate over all tables
    for i, table in enumerate(tables, start=1):
        # get the table headers
        headers = ExtractHTML.get_Table_Headers(table)
        # get all the rows of the table
        rows = ExtractHTML.get_Table_Rows(table)
        # save table as csv file
        table_name = f"{url}-{i}"
        print(f"[+] Saving {table_name}")
        save_As_Csv(table_name, headers, rows)
