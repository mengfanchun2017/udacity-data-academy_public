SELECT DISTINCT o.orderdate, odl.*,TRIM(r.regiondescription) regionname
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