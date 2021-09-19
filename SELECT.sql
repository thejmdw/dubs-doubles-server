-- ALL TIME TOTAL SALES
SELECT
    sum(t.price) AS toppingsales

FROM
    dubsapi_lineitem li
JOIN
    dubsapi_lineitemtopping lit ON lit.line_item_id = li.id
JOIN
    dubsapi_topping t ON lit.topping_id = t.id

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

SELECT 
    COUNT(li.product_id),
    li.product_id,
    p.name
FROM
    dubsapi_lineitem li
JOIN
    dubsapi_product p ON p.id = li.product_id
GROUP BY 
    product_id

