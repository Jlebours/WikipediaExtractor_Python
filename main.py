
import ExtractHTML
import HTMLtoCSV
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    soup = ExtractHTML.UrltoHtml("https://wikipedia.com/wiki/Comparison_(grammar)")
    tables = ExtractHTML.Get_All_Tables(soup)
    print(f"[+] Found a total of {len(tables)} tables.")

    # iterate over all tables
    # iterate over all tables
    for i, table in enumerate(tables, start=1):
        # get the table headers
        headers = ExtractHTML.Get_Table_Headers(table)
        # get all the rows of the table
        rows = ExtractHTML.Get_Table_Rows(table)
        # save table as csv file
        table_name = f"table-{i}"
        print(f"[+] Saving {table_name}")
        HTMLtoCSV.Save_As_Csv(table_name, headers, rows)