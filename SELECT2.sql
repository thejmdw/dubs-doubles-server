SELECT
    o.created_date,
    sum(p.price) AS total_sales,
    row_number() OVER (ORDER BY o.created_date) as id
FROM
    dubsapi_lineitem li
JOIN
    dubsapi_order o ON o.id = li.order_id 
JOIN
    dubsapi_product p ON p.id = li.product_id
JOIN
    dubsapi_customer c ON c.id = o.customer_id
GROUP BY o.created_date

SELECT 
    row_number() OVER (ORDER BY o.created_date) as id
FROM
    (SELECT
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
GROUP BY o.created_date)



