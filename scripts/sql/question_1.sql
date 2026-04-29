-- Question 1)
-- How many active, non delivered, shipments are currently in 
SELECT
  COUNT(*) as active
FROM shipments
WHERE
  stage != 'l) delivered';