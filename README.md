# ZenCargo Data Pipeline

Extracts shipment data from Excel, cleans and validates it, loads it into a SQLite database, and answers analytical questions via SQL displayed in a Jupyter notebook.

## Setup & Run

```bash
uv sync
uv run run.py
```

Then open `display_results.ipynb` to view results.

## Pipeline

| Order | Script | Description |
|-------|--------|-------------|
| 1 | `extract_data.py` | Reads the Excel source file and exports it as a CSV |
| 2 | `clean_data.py` | Runs data quality checks, outputs `data_clean.csv` and `data_quarantine.csv` |
| 3 | `init_db.py` | Creates the SQLite database schema |
| 4 | `load_data.py` | Loads the clean data into the database |

## Questions

| File | Question |
|------|----------|
| `question_1.sql` | How many active (non-delivered) shipments are in the pipeline? |
| `question_2.sql` | What is the average lead time per mode of transport per trade lane? |
| `question_3.sql` | Which shipments have a different estimated vs actual lead time? |

## Docs used

| Library | Link |
|---------|------|
| `sqlite3` | https://docs.python.org/3/library/sqlite3.html |
| `pathlib` | https://docs.python.org/3/library/pathlib.html |
| `datetime` | https://docs.python.org/3/library/datetime.html |
| `pandas` | https://pandas.pydata.org/docs/ |

### Pandas methods

| Method | Link |
|--------|------|
| `pd.read_excel` | https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html |
| `pd.read_csv` | https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html |
| `pd.read_sql_query` | https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html |
| `pd.concat` | https://pandas.pydata.org/docs/reference/api/pandas.concat.html |
| `pd.to_datetime` | https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html |
| `pd.Timestamp` | https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html |
| `pd.Series` | https://pandas.pydata.org/docs/reference/api/pandas.Series.html |
| `DataFrame.copy` | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html |
| `DataFrame.rename` | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html |
| `DataFrame.eq` | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eq.html |
| `DataFrame.any` | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html |
| `DataFrame.isna` | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html |
| `DataFrame.drop_duplicates` | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html |
| `DataFrame.to_csv` | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html |
| `DataFrame.to_sql` | https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html |
| `Series.duplicated` | https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html |
| `Series.gt` | https://pandas.pydata.org/docs/reference/api/pandas.Series.gt.html |
| `Series.astype` | https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html |
| `Series.str.lower` | https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html |
| `Series.str.replace` | https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html |