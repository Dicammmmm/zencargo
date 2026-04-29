-- Question 3)
-- Show the shipments where estimated collection to delivery lead time is different to
-- actual collection to delivery lead 

WITH lead_times AS (
    SELECT
        cargo_id,
        mode_of_transport,
        CAST(
            JULIANDAY(DATE(delivered_latest_estimate_timestamp))
            - JULIANDAY(DATE(collected_latest_estimate_start_datetime_local))
        AS INTEGER) AS estimated_lead_time_days,
        CAST(
            JULIANDAY(DATE(delivered_occurred_at))
            - JULIANDAY(DATE(collected_occurred_at_local))
        AS INTEGER) AS actual_lead_time_days
    FROM shipments
    WHERE delivered_occurred_at IS NOT NULL
      AND collected_occurred_at_local IS NOT NULL
      AND delivered_latest_estimate_timestamp IS NOT NULL
      AND collected_latest_estimate_start_datetime_local IS NOT NULL
)

SELECT *
FROM lead_times
WHERE estimated_lead_time_days != actual_lead_time_days;