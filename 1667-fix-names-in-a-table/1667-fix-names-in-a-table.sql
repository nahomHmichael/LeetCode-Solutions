# Write your MySQL query statement below

SELECT USER_ID, CONCAT(UPPER(SUBSTRING(NAME, 1, 1)), LOWER(SUBSTRING(NAME, 2))) AS NAME
FROM USERS
ORDER BY USER_ID;