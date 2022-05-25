# Write your MySQL query statement below
select T1.name as Employee
from Employee T1
join Employee T2
on T1.managerId=T2.id and T1.salary>T2.salary

# 2nd Approach

Select e1.name as "Employee" from Employee as e1 
where e1.salary > (Select salary from Employee where id= e1.managerId);
