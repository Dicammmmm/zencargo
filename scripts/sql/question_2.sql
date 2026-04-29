-- Question 2)
-- What is the average lead time per mode of transport per trade lane?
SELECT
  s.mode_of_transport,
  cl.country_code AS origin_country,
  dl.country_code AS destination_country,
  COUNT(*) AS n_shipments,
  AVG(
    JULIANDAY(s.delivered_occurred_at) - JULIANDAY(s.collected_occurred_at_local)
  ) AS avg_lead_time_days
FROM shipments s
JOIN locations cl ON s.collection_location_id = cl.location_id
JOIN locations dl ON s.delivered_location_id = dl.location_id
WHERE s.delivered_occurred_at IS NOT NULL
  AND s.collected_occurred_at_local IS NOT NULL
GROUP BY s.mode_of_transport, cl.country_code, dl.country_code
ORDER BY s.mode_of_transport, origin_country, destination_country;