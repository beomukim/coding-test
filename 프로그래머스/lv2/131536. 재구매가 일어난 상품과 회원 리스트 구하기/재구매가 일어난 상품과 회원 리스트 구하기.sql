SELECT 
    USER_ID, PRODUCT_ID
FROM
    ONLINE_SALE
GROUP BY 
    1, 2 
HAVING
    count(product_id) > 1
ORDER BY
    1, 2 desc
