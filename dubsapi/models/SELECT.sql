-- ALL TIME TOTAL SALES
SELECT
    sum(p.price) AS total_sales
FROM
    dubsapi_lineitem li
JOIN
    dubsapi_order o ON o.id = li.order_id 
JOIN
    dubsapi_product p ON p.id = li.product_id
JOIN
    dubsapi_customer c ON c.id = o.customer_id

--DAILY SALES
SELECT
    o.created_date,
    sum(p.price) AS total_sales
FROM
    dubsapi_lineitem li
JOIN
    dubsapi_order o ON o.id = li.order_id 
JOIN
    dubsapi_product p ON p.id = li.product_id
JOIN
    dubsapi_customer c ON c.id = o.customer_id
GROUP BY o.created_date

-- WEEKLY / MONTHLY SALES
SELECT
    o.created_date,
    sum(p.price) AS total_sales
FROM
    dubsapi_lineitem li
JOIN
    dubsapi_order o ON o.id = li.order_id 
JOIN
    dubsapi_product p ON p.id = li.product_id
JOIN
    dubsapi_customer c ON c.id = o.customer_id
GROUP BY o.created_date HAVING o.created_date BETWEEN '2021-09-01' AND '2021-09-31'

DELETE FROM dubsapi_order WHERE id=15;