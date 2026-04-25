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