import pandas
import ExtractHTML
import os


def save_As_Csv(table_name, headers, rows):
    """HTML to CSV for table content of `url` """
    outname = f"{table_name}.csv"
    outdir = './output'
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fullname = os.path.join(outdir, outname)
    pandas.DataFrame(rows, columns=headers).to_csv(fullname)


# All tables of a URL
def createCsv_URL(wurl, url):
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
