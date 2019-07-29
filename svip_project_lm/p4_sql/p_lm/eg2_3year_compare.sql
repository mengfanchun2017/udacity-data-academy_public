-- 找到2014、2015、2016年都增加的销售额的产品

WITH year2014 AS
(
SELECT STRFTIME('%Y', o.OrderDate)ord_date,od.unitprice*od.quantity order_value,p.productId pid
FROM Orders o
JOIN OrderDetails od
ON o.orderId=od.orderId
JOIN Products p
ON od.productId=p.productId
WHERE ord_date='2014'
Group by 3
),

year2015 AS
(
SELECT STRFTIME('%Y', o.OrderDate)ord_date,od.unitprice*od.quantity order_value,p.productId pid
FROM Orders o
JOIN OrderDetails od
ON o.orderId=od.orderId
JOIN Products p
ON od.productId=p.productId
WHERE ord_date='2015'
Group by 3
),

year2016 AS
(
SELECT STRFTIME('%Y', o.OrderDate)ord_date,od.unitprice*od.quantity order_value,p.productId pid
FROM Orders o
JOIN OrderDetails od
ON o.orderId=od.orderId
JOIN Products p
ON od.productId=p.productId
WHERE ord_date='2016'
Group by 3
)

-- 需要注意最后要把三个字表用JOIN的方式进行连接
SELECT year2014.pid, year2014.order_value AS value2014, 
year2015.order_value AS value2015,
year2016.order_value AS value2016
FROM year2014
JOIN year2015
ON year2014.pid = year2015.pid
JOIN year2016
ON year2016.pid = year2015.pid
-- 用WHERE过滤出3年产品销量逐渐增加的
WHERE value2016 > value2015 AND value2015 > value2014 
;