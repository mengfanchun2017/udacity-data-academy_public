WITH t2 AS
(SELECT ord_year,regionname,productid,SUM(quantity) AS product_qty,SUM(ord_usd) AS product_usd
FROM 
(SELECT STRFTIME('%Y',orderdate) ord_year,
orderid,productid,quantity,unitprice*quantity-discount*unitprice*quantity AS ord_usd,regionname
FROM t1)
GROUP BY 1,2,3
ORDER BY 5 DESC)

SELECT t2.*
FROM t2