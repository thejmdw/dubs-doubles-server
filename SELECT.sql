-- ALL TIME TOTAL PRODUCT SALES
SELECT
    sum(p.price) AS productsales

FROM
    dubsapi_lineitem li
JOIN
    dubsapi_order o ON o.id = li.order_id 
JOIN
    dubsapi_product p ON p.id = li.product_id
JOIN
    dubsapi_customer c ON c.id = o.customer_id

--ALL TIME TOTAL TOPPING SALES
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
-- HAVING 
--     o.created_date = '2021-09-06'

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
GROUP BY 
    o.created_date 
HAVING 
    o.created_date BETWEEN '2021-09-01' AND '2021-09-07'

DELETE FROM dubsapi_order WHERE id=15;


SELECT 
    sum(total_sales)
FROM (
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
GROUP BY o.created_date HAVING o.created_date BETWEEN '2021-09-01' AND '2021-09-07')




-- SINGLE PRODUCT COUNT/TOTAL PRODUCTS COUNT
SELECT 
    COUNT(li.product_id),
    li.product_id,
    p.name,
    row_number() OVER (ORDER BY COUNT(li.product_id) DESC) as id
FROM
    dubsapi_lineitem li
JOIN
    dubsapi_product p ON p.id = li.product_id
GROUP BY 
    product_id 
-- HAVING 
--     product_id = 24

SELECT 
    COUNT(lit.topping_id) AS topping_count,
    lit.topping_id,
    t.name
FROM
    dubsapi_lineitemtopping lit
JOIN
    dubsapi_topping t ON t.id = lit.topping_id
GROUP BY 
    topping_id
-- HAVING
--     topping_id = 2

SELECT
    *
FROM
    dubsapi_order