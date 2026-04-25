import pandas as pd
from pathlib import Path
from clean_data_utils import DataQuality

DATA_ROOT = "./data/"
DATA = "data.csv"


def main():
    dq = DataQuality(DATA)
    (
        dq._quarantine_duplicate_cargo_id()
        ._remove_missing_values()
        ._quarantine_invalid_dates()
        ._quarantine_unknowns()
    )

    dq.clean.to_csv(Path(DATA_ROOT) / "data_clean.csv", index=False)
    dq.quarantine.to_csv(Path(DATA_ROOT) / "data_quarantine.csv", index=False)


if __name__ == "__main__":
    main()
