import HTMLtoCSV
import ExtractHTML

if __name__ == '__main__':
    print("Reading url file...")
    # Two dimensional tab with urls and it's name for each one
    allUrls = ExtractHTML.read_urls()
    print(f"You will extract tables from {len(allUrls)} urls")
    print("Starting extraction...")
    for url, name in allUrls:
        tables = ExtractHTML.get_tables(url)
        HTMLtoCSV.convert_csv(tables, name)
    print("End of extraction, you can check the output directory :)")


