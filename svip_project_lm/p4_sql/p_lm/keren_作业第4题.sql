WITH S1 AS
(
SELECT STRFTIME('%Y', o.OrderDate)ord_date,od.unitprice*od.quantity AS order_value,p.productId,p.ProductName
FROM Orders o
JOIN OrderDetails od
ON o.orderId=od.orderId
JOIN Products p
ON od.productId=p.productId
WHERE ord_date='2014'
Group by 3,1
),

S2 AS
(
SELECT STRFTIME('%Y', o.OrderDate)ord_date,od.unitprice*od.quantity AS order_value,p.productId,p.ProductName
FROM Orders o
JOIN OrderDetails od
ON o.orderId=od.orderId
JOIN Products p
ON od.productId=p.productId
WHERE ord_date='2015'
Group by 3,1
),

S3 AS
(
SELECT STRFTIME('%Y', o.OrderDate)ord_date,od.unitprice*od.quantity AS order_value,p.productId,p.ProductName
FROM Orders o
JOIN OrderDetails od
ON o.orderId=od.orderId
JOIN Products p
ON od.productId=p.productId
WHERE ord_date='2016'
Group by 3,1
),

SELECT S1.Order_value AS '2014',S2.Order_value AS '2015',S3.Order_value AS '2016'
FROM S1
JOIN S2
On S1.productId=S2.ProductID
JOIN S3
On S2.productID=S3.ProductID