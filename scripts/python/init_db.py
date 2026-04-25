import sqlite3
from pathlib import Path

DATA_ROOT = Path("./data/")
SCRIPTS_ROOT = Path("./scripts/")


def main():
    con = sqlite3.connect(DATA_ROOT / "database.db")

    with open(SCRIPTS_ROOT / "sql" / "data_model.sql", "r") as f:
        con.executescript(f.read())

    con.close()


if __name__ == "__main__":
    main()
