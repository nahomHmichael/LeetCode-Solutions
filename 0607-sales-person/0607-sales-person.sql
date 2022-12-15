# Write your MySQL query statement below

WITH cte AS
(SELECT sales_id FROM Orders o
LEFT JOIN Company c On o.com_id = c.com_id
WHERE c.name LIKE 'RED')

SELECT name
FROM SalesPerson
WHERE sales_id  NOT IN (SELECT DISTINCT
sales_id FROM cte)