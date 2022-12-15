# Write your MySQL query statement below
SELECT firstName, lastName, city, state FROM Person P
LEFT OUTER JOIN Address A ON P.PersonId = A.PersonId
