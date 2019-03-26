WITH t1 AS
(SELECT DISTINCT o.orderdate, odl.*,TRIM(r.regiondescription) regionname
FROM orderdetails odl
JOIN orders o
ON odl.orderid=o.orderid
JOIN employeeterritories et
ON o.employeeid=et.employeeid
JOIN territories t
ON et.territoryid=t.territoryid
JOIN region r
ON r.regionid=t.regionid
WHERE o.orderdate BETWEEN '2015-01-01' AND '2015-12-31'
GROUP BY o.orderdate),

t2 AS
(SELECT ord_year,regionname,productid,SUM(quantity) AS product_qty,SUM(ord_usd) AS product_usd
FROM 
(SELECT STRFTIME('%Y',orderdate) ord_year,
orderid,productid,quantity,unitprice*quantity-discount*unitprice*quantity AS ord_usd,regionname
FROM t1)
GROUP BY 1,2,3
ORDER BY 5 DESC),

t3 AS
(SELECT p.productid,p.productname,c.categoryid,c.categoryname
FROM products p
JOIN categories c
ON p.categoryid=c.categoryid)

SELECT t2*,t3.productname,t3.categoryname
FROM t3
JOIN t2
ON t2.productid=t3.productid