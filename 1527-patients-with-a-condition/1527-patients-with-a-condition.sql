# Write your MySQL query statement below

SELECT PATIENT_ID, PATIENT_NAME, CONDITIONS
FROM PATIENTS
WHERE CONDITIONS LIKE "%DIAB1%"
AND CONDITIONS NOT LIKE "SADIAB1%"