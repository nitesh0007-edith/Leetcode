# Write your MySQL query statement below
select T1.name as Employee
from Employee T1
join Employee T2
on T1.managerId=T2.id and T1.salary>T2.salary
