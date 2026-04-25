import sqlite3
import pandas as pd
from pathlib import Path

DATA_ROOT = "./data/"

conn = sqlite3.connect(Path(DATA_ROOT) / "database.db")
data = pd.read_csv(Path(DATA_ROOT) / "data_clean.csv", index_col=0)


def _prep_locations(df: pd.DataFrame) -> pd.DataFrame:
    collection_locations = df[
        [
            "collection_location_id",
            "collection_location_street",
            "collection_location_city",
            "collection_location_country_code",
        ]
    ].copy()
    collection_locations.columns = ["location_id", "street", "city", "country_code"]

    delivery_locations = df[
        [
            "delivered_location_id",
            "delivered_location_street",
            "delivered_location_city",
            "delivered_location_country_code",
        ]
    ].copy()
    delivery_locations.columns = ["location_id", "street", "city", "country_code"]

    locations = pd.concat([collection_locations, delivery_locations]).drop_duplicates(
        subset="location_id"
    )

    return locations


def _prep_shipments(df: pd.DataFrame) -> pd.DataFrame:
    shipments = df[
        [
            "cargo_id",
            "mode_of_transport",
            "stage",
            "requested_timestamp",
            "collection_location_id",
            "collected_latest_estimate_start_datetime_local",
            "collected_occurred_at_local",
            "delivered_location_id",
            "delivered_latest_estimate_timestamp",
            "delivered_occurred_at",
            "revenue_date",
            "vat_applicable",
            "invoice_uploaded_at",
        ]
    ]

    return shipments


def _insert_data(locations: pd.DataFrame, shipments: pd.DataFrame) -> None:
    locations.to_sql("locations", conn, if_exists="replace", index=False)
    shipments.to_sql("shipments", conn, if_exists="replace", index=False)


def main():
    locations, shipments = _prep_locations(data), _prep_shipments(data)
    _insert_data(locations, shipments)

    conn.close()


if __name__ == "__main__":
    main()
