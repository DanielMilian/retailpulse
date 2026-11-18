import pandas as pd

FILE_PATH = "data/raw/uci/online_retail_II.xlsx"

excel = pd.ExcelFile(FILE_PATH)

print("Available sheets:", excel.sheet_names)

for sheet in excel.sheet_names:
    df = pd.read_excel(FILE_PATH, sheet_name=sheet)

    print(f"\n{'=' * 50}")
    print(f"SHEET: {sheet}")
    print(f"{'=' * 50}")

    print("\nShape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

