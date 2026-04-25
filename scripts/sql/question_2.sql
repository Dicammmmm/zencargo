-- Question 2)
-- What is the average lead time per mode of transport per trade lane?

SELECT
  s.mode_of_transport,
  cl.country_code AS origin_country,
  dl.country_code AS destination_country,
  AVG(
    JULIANDAY(s.delivered_occurred_at) - JULIANDAY(s.collected_occurred_at_local)
  ) AS avg_lead_time_days