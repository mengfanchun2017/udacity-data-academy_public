## 对于布尔数
print('---bools---')
a = True
b = False
print (a & b)  # 输出False
print (a | b)  # 输出True
print (a and b)  # 输出False
print (a or b)  # 输出True

## 对于列表
print('---list---')
a_list = [True, False, True]
b_list = [True, True, False]
# print (a_list & b_list)  # 不注释掉会报错
# print (a_list | b_list)  # 不注释掉会报错
print (a_list and b_list)  # 输出[True, True, False]
print (a_list or b_list)  # 输出[True, False, True]

## 对于pandas中的Series
print('---series---')
import pandas as pd
df = pd.DataFrame({'a': [True, False, True], 'b': [True, True, False]})
print (df)
print (df['a'] & df['b'])
print (df['a'] | df['b'])

# print (df['a'] and df['b'])  # error
# print df['a'] or df['b']  # error

## 对于numpy中的ndarray
print('---ndarray---')
import numpy as np
a_arr = np.array([True, False, True])
b_arr = np.array([True, True, False])
print (a_arr & b_arr)
print (a_arr | b_arr)

# print (a_arr and b_arr)  # error
# print a_arr or b_arr  # error
# 使用logical_and/or进行逻辑与操作
print(np.logical_and(a_arr, b_arr))

import numpy as np

## time测试
from timeit import timeit, repeat

a1 = np.array([True, False, True, True, False])
b1 = np.array([True, True, False, False, True])
a2 = np.array([1, 0, 1, 1, 0])
b2 = np.array([1, 1, 0, 0, 1])

# 定义2维的ndarray（注意，经测试如果用True和False没有改善）
a3 = np.array([
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1]])
b3 = np.array([
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 1]])

def compare1():
    r1 = a1 & b1
    r2 = a1 | b1
    #print(r1, r2)
    return r1, r2
t1 = min(repeat('compare1()', 'from __main__ import compare1', number=100000, repeat=10))
print(t1)

def compare1b():
    r1 = np.logical_and(a1, b1)
    r2 = np.logical_or(a1, b1)
    return r1, r2
# 使用timeit是重复的，因为cpu有占用，所以用repeat进行多次，取最小的
# t2 = timeit('compare1b()', 'from __main__ import compare1b', number=100000)
t2 = min(repeat('compare1b()', 'from __main__ import compare1b', number=100000, repeat=10))

# 定义两种方式的比较函数
def compare1s():
    return a3 & b3, a3 | b3

def compare1bs():
    return np.logical_and(a3, b3), np.logical_or(a3, b3)

# 使用timeit是重复的，因为cpu有占用，所以用repeat进行多次，取最小的
# 如果不用repeat可以直接使用timeit如下：
# t = timeit('compare1b()', 'from __main__ import compare1b', number=100000)
# timeit的中文参考：https://www.cnblogs.com/PrettyTom/p/6657984.html
# timeit官方文档：https://docs.python.org/3/library/timeit.html

t3 = min(repeat('compare1s()', 'from __main__ import compare1s', number=100000, repeat=10))
t4 = min(repeat('compare1bs()', 'from __main__ import compare1bs', number=100000, repeat=10))

print(t3, t4, t4 / t3)

# logical_and官方文档：https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.logical_and.html

