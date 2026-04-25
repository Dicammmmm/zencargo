import sqlite3
from pathlib import Path

DATA_ROOT = "./data/"
SCRIPTS_ROOT = "./scripts/"


def main():
    con = sqlite3.connect(Path(DATA_ROOT) / "database.db")

    with open(Path(SCRIPTS_ROOT) / "data_model.sql", "r") as f:
        con.executescript(f.read())

    con.close()


if __name__ == "__main__":
    main()
