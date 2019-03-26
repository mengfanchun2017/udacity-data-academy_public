import pandas as pd

# Subway ridership for 5 stations on 10 different days
ridership_df = pd.DataFrame(
    data=[[   0,    0,    2,    5,    0],
          [1478, 3877, 3674, 2328, 2539],
          [1613, 4088, 3991, 6461, 2691],
          [1560, 3392, 3826, 4787, 2613],
          [1608, 4802, 3932, 4477, 2705],
          [1576, 3933, 3909, 4979, 2685],
          [  95,  229,  255,  496,  201],
          [   2,    0,    1,   27,    0],
          [1438, 3785, 3589, 4174, 2215],
          [1342, 4043, 4009, 4665, 3033]],
    index=['05-01-11', '05-02-11', '05-03-11', '05-04-11', '05-05-11',
           '05-06-11', '05-07-11', '05-08-11', '05-09-11', '05-10-11'],
    columns=['R003', 'R004', 'R005', 'R006', 'R007']
)

print(ridership_df.head())

# 用index定义行名，用columns定义列名

# Change False to True for each block of code to see what it does

# DataFrame creation
if 1:
    # You can create a DataFrame out of a dictionary mapping column names to values
    df_1 = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print (df_1)

    # You can also use a list of lists or a 2D NumPy array
    df_2 = pd.DataFrame([[0, 1, 2], [3, 4, 5]], columns=['A', 'B', 'C'])
    print (df_2)


# Accessing elements
if 0:
    print (ridership_df.iloc[0])
    print (ridership_df.loc['05-05-11'])
    print (ridership_df['R003'])
    print (ridership_df.iloc[1, 3])
    # .iloc[x]是按位置定位行
    # .loc['x']是按照名字定位行
    # [colname]是选择列
    # .iloc[x,y]是定位行和列（也就是1个元素了）

# Accessing multiple rows
if 0:
    print (ridership_df.iloc[1:4])
    # [x:y]表示二维表中的一个范围

# Accessing multiple columns
if 0:
    print (ridership_df[['R003', 'R005']])
    # 此处是选择多列

# Pandas axis
if 0:
    df = pd.DataFrame({'A': [0, 1, 2], 'B': [3, 4, 5]})
    print (df.sum())
    # 按照列做汇总
    print (df.sum(axis=1))
    # 按照行做汇总
    print (df.values.sum())
    # 把所有值做汇总

def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.

    This is the same as a previous exercise, but this time the
    input is a Pandas DataFrame rather than a 2D NumPy array.
    '''
    overall_mean = ridership.values.mean()
    # DataFrame使用.values.mean()计算所有的平均值
    max_station = ridership_df.iloc[0].argmax()
    # 此处和arrays不同，使用iloc[0].argmax()找出在0行最大的列值在那里
    mean_for_max = ridership[max_station].mean()
    # 再把这个列的所有值做平均，就能得出这个车站的平均值了

    return (overall_mean, mean_for_max)

print(mean_riders_for_max_station(ridership_df))
