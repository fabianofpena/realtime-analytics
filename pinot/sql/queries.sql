-- Total orders in the last hour
SELECT COUNT(1) FROM enriched_orders WHERE request_time > toDateTime(now() - 60 * 60 * 1000, 'yyyy-MM-dd HH:mm:ss Z') 

-- Total revenue from orders in the last hour
select sum(total_amount) from enriched_orders where request_time > toDateTime(now() - 60 * 60 * 1000, 'yyyy-MM-dd HH:mm:ss Z') 

-- Average revenue per user in the last hour
select avg(total_amount) from enriched_orders where request_time > toDateTime(now() - 60 * 60 * 1000, 'yyyy-MM-dd HH:mm:ss Z') 

-- Total orders and total revenue by city in the last hour
select count(1), sum(total_amount), city from enriched_orders where request_time > toDateTime(now() - 60 * 60 * 1000, 'yyyy-MM-dd HH:mm:ss Z')  group by city order by count(*) desc

-- Total completed orders by a single customer
select count(1) from enriched_orders where  request_time > toDateTime(now() - 60 * 60 * 1000, 'yyyy-MM-dd HH:mm:ss Z') 
