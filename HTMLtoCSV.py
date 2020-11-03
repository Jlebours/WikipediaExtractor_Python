import pandas as pd
import ExtractHTML


def save_As_Csv(table_name, headers, rows):
    """HTML to CSV for table content of `url` """
    pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv")


# All tables of a URL
def CreateCsv_URL(url):
    soup = ExtractHTML.UrltoHtml(url)
    tables = ExtractHTML.Get_All_Tables(soup)
    print(f"[+] Found a total of {len(tables)} tables.")

    # iterate over all tables
    for i, table in enumerate(tables, start=1):
        # get the table headers
        headers = ExtractHTML.Get_Table_Headers(table)
        # get all the rows of the table
        rows = ExtractHTML.Get_Table_Rows(table)
        # save table as csv file
        table_name = f"table-{i}"
        print(f"[+] Saving {table_name}")
        save_As_Csv(table_name, headers, rows)
