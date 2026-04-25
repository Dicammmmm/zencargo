CREATE TABLE  IF NOT EXISTS locations (
  location_id TEXT PRIMARY KEY,
  street TEXT,
  city TEXT,
  country_code TEXT
);

CREATE TABLE IF NOT EXISTS shipments (
  cargo_id TEXT PRIMARY KEY,
  mode_of_transport TEXT,
  stage TEXT,
  requested_timestamp TIMESTAMP,
  collection_location_id TEXT REFERENCES locations(location_id),
  collected_latest_estimate_start_datetime_local TIMESTAMP,
  collected_occurred_at_local TIMESTAMP,
  delivered_location_id TEXT REFERENCES locations(location_id),
  delivered_latest_estimate_timestamp TIMESTAMP,
  delivered_occurred_at TIMESTAMP,
  revenue_date DATE,
  vat_applicable BOOLEAN,
  invoice_uploaded_at TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_shipments_collection_location_id ON shipments(collection_location_id);
CREATE INDEX IF NOT EXISTS idx_shipments_delivered_location_id ON shipments(delivered_location_id);