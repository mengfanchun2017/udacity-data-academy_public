## solution1
# for 3 same color
p3 = (5/17)*(4/16)

# for 2 same color 分为以下3种情况
## 2、3同色,1异色
p2c = (12/17)*(5/16)
## 1、2同色,3异色
p2a = (5/17)*(12/16)
## 1、3同色,2异色
p2b = (12/17)*(5/16)

# for none same color
p1 = (12/17)*(6/16)

# results
print('\n\n-check p-')
print(p3,p2a,p2b,p2c,p1)
print('-check Q2-')
print(p3+p2a+p2b+p2c)
# 最后来个全概率检查(各种概率加一起应该为1)
print('-check if full =1-')
print(p3+p2a+p2b+p1+p2c)