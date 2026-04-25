import pandas as pd
from datetime import date

MAX_DATE = date.today()


class DataQuality:
    def __init__(self, data: pd.DataFrame):
        self.clean = data.copy()
        self.quarantine = pd.DataFrame()

    def _quarantine(self, mask: pd.Series):
        self.quarantine = pd.concat([self.quarantine, self.clean[mask]])
        self.clean = self.clean[~mask]
        return self

    def _invalid_value(self, value):
        mask = self.clean.eq(value).any(axis=1)
        return self._quarantine(mask)

    def _quarantine_duplicate_cargo_id(self):
        mask = self.clean["cargo_id"].duplicated(keep=False)
        return self._quarantine(mask)

    def _remove_missing_values(self):
        mask = (
            self.clean[
                [
                    "requested_timestamp",
                    "collection_location_street",
                    "collection_location_city",
                    "delivered_location_street",
                    "delivered_location_city",
                ]
            ]
            .isna()
            .any(axis=1)
        )
        return self._quarantine(mask)

    def _quarantine_invalid_dates(self):
        future_dates_mask = (
            self.clean[
                [
                    "requested_timestamp",
                    "collected_latest_estimate_start_datetime_local",
                    "collected_occurred_at_local",
                    "delivered_latest_estimate_timestamp",
                    "delivered_occurred_at",
                    "invoice_uploaded_at",
                    "revenue_date",
                ]
            ]
            .gt(MAX_DATE)
            .any(axis=1)
        )

        revenue_mask = (
            pd.to_datetime(self.clean["revenue_date"]).dt.date
            < pd.to_datetime(self.clean["requested_timestamp"]).dt.date
        )
        mask = future_dates_mask | revenue_mask
        return self._quarantine(mask)

    def _quarantine_unknowns(self):
        self._invalid_value("Unknown")
        return self._invalid_value("00000000-0000-0000-0000-000000000000")

    def _rename_columns(self):
        self.clean = self.clean.rename(
            columns={
                "modeoftransport": "mode_of_transport",
                "deliveredLocationId": "delivered_location_id",
            }
        )
        self.clean["stage"] = self.clean["stage"].str.lower()
        return self
