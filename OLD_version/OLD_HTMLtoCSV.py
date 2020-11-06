import pandas
import ExtractHTML
import os


def createCsv_URL(wurl, url):
    soup = ExtractHTML.urlToHtml(wurl)
    tables = ExtractHTML.get_All_Tables(soup)
    print(f"[+] Found a total of {len(tables)} tables.")
    # iterate over all tables
    for i, table in enumerate(tables, start=1):
        # get the table headers
        headers = ExtractHTML.get_headers(table)
        # get all the rows of the table
        rows = ExtractHTML.get_rows(table)
        # save table as csv file
        table_name = f"{url}-{i}"
        print(f"[+] Saving {table_name}")
        save_As_Csv(table_name, headers, rows)


def save_As_Csv(table_name, headers, rows):
    outname = f"{table_name}.csv"
    outdir = './output'
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    fullname = os.path.join(outdir, outname)
    pandas.DataFrame(rows, columns=headers).to_csv(fullname, index=False)
