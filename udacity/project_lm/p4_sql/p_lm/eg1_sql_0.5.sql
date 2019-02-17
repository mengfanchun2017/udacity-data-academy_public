--建议1:不要使用t1，t2这种不好辨认的名字，建议使用有意义的
--比如t1可以改为data_and_region
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

--建议2:之所以报错是因为在最后的SELECT中使用了JOIN
--建议这种复杂的情况在WITH中完成JOIN的功能
--最后的代码只是完成WITH中别名数据间的串接
SELECT t2.*, t3.productname, t3.categoryname
FROM t2, t3

--建议3:过滤的思路是：
--	先做GROUP BY进行拆分（按照你的要求）
--	再做ORDER BY加DESC进行反向排列
--	最后LIMIT设定输出的数量

--建议4:你的想法是：
--“每个区域前三的产品“
--根据现在下面的输出，有几点检查建议：
--1、year时间在t1中已经有了限定，所以其实在输出时候不用选择出来
--2、product_id和productname有些不一致
--3、根据问题，如果是找前三的产品（product），那么对于cate的所有操作都没有必要了，可以简化查询