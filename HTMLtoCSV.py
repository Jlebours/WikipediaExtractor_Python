import pandas as pd

def Save_As_Csv(table_name, headers, rows):
    """HTML to CSV for table content of `url` """

    pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv")