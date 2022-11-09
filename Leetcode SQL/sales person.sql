# Write your MySQL query statement below
select name from SalesPerson where name not in(
select T1.name 
from SalesPerson T1
join Orders T2 on T1.sales_id=T2.sales_id
join Company T3 on T2.com_id=T3.com_id
where T3.name  like 'RED')
