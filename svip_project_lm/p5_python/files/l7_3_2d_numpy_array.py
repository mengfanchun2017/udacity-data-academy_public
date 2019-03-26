import numpy as np

# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [   0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [  95,  229,  255,  496,  201],
    [   2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])

# Change False to True for each block of code to see what it does

# Accessing elements
if 0:
    print(ridership[1, 3])
    print(ridership[1:3, 3:5])
    print(ridership[1, :])

# Vectorized operations on rows or columns
if 0:
    print(ridership[0, :] + ridership[1, :])
    print(ridership[:, 0] + ridership[:, 1])

# Vectorized operations on entire arrays
if 0:
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    print(a + b)

def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.

    Hint: NumPy's argmax() function might be useful:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html
    '''
    max_station = ridership[0,:].argmax()
    # 通过argmax检查第1行那个值最大，如果想看看中间输出，把下面行#去掉打印看看
    #print(ridership[0,:])

    # [0,:]代表选中第一天的所有车站出入量，就是从[0 0 2 5 0]中选
    # 结果是第4个元素5最大，所以max_station = 3
    # argmax就是求最大元素的位置，注意是从0开始，所以第四个元素是3
    mean_for_max = ridership[:,max_station].mean()
    # 那么接下来要算这个车站的平均数，就把这个车站所有的数量取平均
    # [:,max_station]带入3就是[:,3]就是说第4列的所有值
    # ：的意思是选中所有内容
    overall_mean = ridership.mean()
    # 这行代码是计算整体的客流量平均值
    return (overall_mean, mean_for_max)

print(mean_riders_for_max_station(ridership))

# 扩展，ragmax可以加axis参数，代表计算2d数组中横向切分和纵向切分的最大值位置
# 下面行将会返回每一列的最大值在那里
#print(ridership.argmax(axis = 0))
