
SELECT
    Product,
    Sub_product,
    SUM(CASE WHEN EXTRACT(YEAR FROM Date_received) = 2023 AND EXTRACT(QUARTER FROM Date_received) = 1 THEN 1 ELSE 0 END) AS Q1,
    SUM(CASE WHEN EXTRACT(YEAR FROM Date_received) = 2023 AND EXTRACT(QUARTER FROM Date_received) = 2 THEN 1 ELSE 0 END) AS Q2,
    SUM(CASE WHEN EXTRACT(YEAR FROM Date_received) = 2023 AND EXTRACT(QUARTER FROM Date_received) = 3 THEN 1 ELSE 0 END) AS Q3,
    SUM(CASE WHEN EXTRACT(YEAR FROM Date_received) = 2023 AND EXTRACT(QUARTER FROM Date_received) = 4 THEN 1 ELSE 0 END) AS Q4
FROM
    complaints
WHERE
    EXTRACT(YEAR FROM Date_received) = 2023
GROUP BY
    Product,
    Sub_product
ORDER BY
    Product,
    Sub_product;