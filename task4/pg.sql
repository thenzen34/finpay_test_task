/*
select
       count(*)
from phones p
join items i on i.user_id = any(p.users) and i.status = 7
where p.phone in ('1', '2')
 */


select
       sum(case when i.status = 7 then 1 else 0 end) as win,
       sum(case when i.status = 3 then 1 else 0 end) as lose
from phones p
join items i on i.user_id = any(p.users)
where p.phone in (...)
