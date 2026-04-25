from pathlib import Path
import pandas as pd


DATA_ROOT = Path("../../data")


def _read_excel(excel_file: str) -> pd.DataFrame:
    DATA_SHEET = "Data Source"
    excel_df = pd.read_excel(
        DATA_ROOT / excel_file, engine="openpyxl", sheet_name=DATA_SHEET
    )

    return excel_df


def _export_csv(excel_df: pd.DataFrame) -> None:
    excel_df.to_csv(DATA_ROOT / "data.csv")


def main():
    data = _read_excel("data_source.xlsx")
    _export_csv(data)


if __name__ == "__main__":
    main()
