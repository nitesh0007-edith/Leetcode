# Write your MySQL query statement below
SELECT T1.player_id, T1.event_date as first_login
FROM Activity T1
INNER JOIN 
(
    SELECT player_id, MIN(event_date) as MinDate FROM Activity GROUP BY player_id
) as T2
on T1.player_id=T2.player_id and T1.event_date=T2.MinDate
