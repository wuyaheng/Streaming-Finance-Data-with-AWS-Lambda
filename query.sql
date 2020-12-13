SELECT SPLIT_PART(ID,',',1) as name, max_high, SPLIT_PART(ID,',',3) as ts, SPLIT_PART(ID,',',2) as hour FROM
(SELECT DISTINCT(ID), max_high FROM
(SELECT CONCAT(name,',',hour,',',ts) AS ID, max_high FROM (SELECT A.name, A.hour, A.ts, B.max_high FROM (SELECT name, high, ts, SUBSTRING(ts, 12, 2) AS hour  FROM stocks.sta9760f2020datastream) A
INNER JOIN (SELECT name, SUBSTRING(ts, 12, 2) AS hour, MAX(high) AS max_high FROM stocks.sta9760f2020datastream GROUP BY name, SUBSTRING(ts, 12, 2)) B
ON A.name = B.name AND A.hour = B.hour AND A.high = B.max_high)))
ORDER BY name, hour;