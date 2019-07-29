SELECT STRFTIME('%Y', o.OrderDate)ord_date,od.unitprice*od.quantity order_value,p.productId,p.ProductName
FROM Orders o
JOIN OrderDetails od
ON o.orderId=od.orderId
JOIN Products p
ON od.productId=p.productId
WHERE ord_date='2014'
Group by 3