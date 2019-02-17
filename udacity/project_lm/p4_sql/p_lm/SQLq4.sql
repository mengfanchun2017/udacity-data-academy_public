WITH raclette AS (
SELECT STRFTIME('%Y-%m',o.OrderDate) AS YearMonth, SUM(p.UnitPrice*od.Quantity) AS Raclette
FROM Products p
JOIN OrderDetails od
ON p.ProductID = od.ProductID
JOIN Orders o
ON o.OrderID = od.OrderID
WHERE DATE(o.OrderDate) < STRFTIME('2016-05-01') AND p.ProductName IN ('Raclette Courdavault')
GROUP BY YearMonth
ORDER BY YearMonth),

camembert AS (
SELECT STRFTIME('%Y-%m',o.OrderDate) AS YearMonth, SUM(p.UnitPrice*od.Quantity) AS Camembert
FROM Products p
JOIN OrderDetails od
ON p.ProductID = od.ProductID
JOIN Orders o
ON o.OrderID = od.OrderID
WHERE DATE(o.OrderDate) < STRFTIME('2016-05-01') AND p.ProductName IN ('Camembert Pierrot')
GROUP BY YearMonth
ORDER BY YearMonth),

tarte AS (
SELECT STRFTIME('%Y-%m',o.OrderDate) AS YearMonth, SUM(p.UnitPrice*od.Quantity) AS Tarte
FROM Products p
JOIN OrderDetails od
ON p.ProductID = od.ProductID
JOIN Orders o
ON o.OrderID = od.OrderID
WHERE DATE(o.OrderDate) < STRFTIME('2016-05-01') AND p.ProductName IN ('Tarte au sucre')
GROUP BY YearMonth
ORDER BY YearMonth),

gnocchi AS (
SELECT STRFTIME('%Y-%m',o.OrderDate) AS YearMonth, SUM(p.UnitPrice*od.Quantity) AS Gnocchi
FROM Products p
JOIN OrderDetails od
ON p.ProductID = od.ProductID
JOIN Orders o
ON o.OrderID = od.OrderID
WHERE DATE(o.OrderDate) < STRFTIME('2016-05-01') AND p.ProductName IN ('Gnocchi di nonna Alice')
GROUP BY YearMonth
ORDER BY YearMonth),

manjimup AS (
SELECT STRFTIME('%Y-%m',o.OrderDate) AS YearMonth, SUM(p.UnitPrice*od.Quantity) AS Manjimup
FROM Products p
JOIN OrderDetails od
ON p.ProductID = od.ProductID
JOIN Orders o
ON o.OrderID = od.OrderID
WHERE DATE(o.OrderDate) < STRFTIME('2016-05-01') AND p.ProductName IN ('Manjimup Dried Apples')
GROUP BY YearMonth
ORDER BY YearMonth)

SELECT r.YearMonth, r.Raclette, c.Camembert, t.Tarte, g.Gnocchi, m.Manjimup
FROM raclette AS r
LEFT JOIN camembert AS c
ON r.YearMonth = c.YearMonth
LEFT JOIN tarte AS t
ON r.YearMonth = t.YearMonth
LEFT JOIN gnocchi AS g
ON r.YearMonth = g.YearMonth
LEFT JOIN manjimup m
ON r.YearMonth = m.YearMonth
ORDER BY r.YearMonth