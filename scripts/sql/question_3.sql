-- Question 3)
-- Show the shipments where estimated collection to delivery lead time is different to
-- actual collection to delivery lead 

SELECT
  cargo_id,
  mode_of_transport,
  ROUND(JULIANDAY(delivered_latest_estimate_timestamp) - JULIANDAY(collected_latest_estimate_start_datetime_local), 2) AS estimated_lead_time_days,
  ROUND(JULIANDAY(delivered_occurred_at) - JULIANDAY(collected_occurred_at_local), 2) AS actual_lead_time_days
FROM shipments
WHERE delivered_occurred_at IS NOT NULL
  AND collected_occurred_at_local IS NOT NULL
  AND delivered_latest_estimate_timestamp IS NOT NULL
  AND collected_latest_estimate_start_datetime_local IS NOT NULL
  AND ROUND(JULIANDAY(delivered_latest_estimate_timestamp) - JULIANDAY(collected_latest_estimate_start_datetime_local), 2)
   != ROUND(JULIANDAY(delivered_occurred_at) - JULIANDAY(collected_occurred_at_local), 2);