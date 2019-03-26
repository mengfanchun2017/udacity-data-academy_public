WITH top20 AS(
SELECT TRIM(r.regiondescription) regionname, od.productid id, od.UnitPrice*od.Quantity*(1-od.Discount) order_usd
FROM OrderDetails od
JOIN Orders o
ON od.orderid=o.orderid
JOIN EmployeeTerritories et
ON o.employeeid=et.employeeid
JOIN Territories t
ON et.territoryid=t.territoryid
JOIN Region r
ON r.regionid=t.regionid
WHERE o.orderdate BETWEEN '2015-01-01' AND '2015-12-31'
GROUP BY productid
ORDER BY order_usd DESC
LIMIT 20)

-- sqlite中没有很好的方法
-- 需要写一个很复杂的子查询递归
-- pass掉，复杂的数据规整功能放在python中实现
-- https://stackoverflow.com/questions/2643314/mysql-group-by-limit
-- 这里使用前20个（top20 product代替原数据）

--WITH plus1 AS(
--SELECT top20.*, categoryname
--FROM top20
--JOIN products p


SELECT top20.*, pr.productname, ca.categoryname
FROM  top20
JOIN Products pr
ON top20.id = pr.productid
JOIN Categories ca
ON pr.categoryid = ca.categoryid
