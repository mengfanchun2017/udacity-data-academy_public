SELECT STRFTIME('%Y', o.OrderDate)ord_date,od.unitprice*od.quantity order_value,p.productId,p.ProductName
FROM Orders o
JOIN OrderDetails od
ON o.orderId=od.orderId
JOIN Products p
ON od.productId=p.productId
WHERE ord_date BETWEEN '2014' AND '2016'
Group by 1,3