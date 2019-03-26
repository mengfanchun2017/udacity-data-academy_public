import numpy as np
import pandas as pd

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

#print(example_df)

# Change False to True for each block of code to see what it does

# Standardize each group
if 0:
    def standardize(xs):
        return (xs - xs.mean()) / xs.std()
    grouped_data = example_df.groupby('even')
    print(grouped_data)
    print()
    #只打印groupby的输出是一个提示，因为没有指定要打印分组之后的什么东西
    print(grouped_data['value'].apply(standardize))
    #使用.apply将grouped_data分组后的value的值进行标准化计算

# Find second largest value in each group
if 0:
    def second_largest(xs):
        sorted_xs = xs.sort_values(inplace=False, ascending=False)
        #如果报错'Series' object has no attribute 'sort'
        #是因为pandas版本已经比实例中的高
        #将sort改为sort_values
        return sorted_xs.iloc[1]
    # 先对输出排序，再使用.iloc[1]输出排序后的第二个元素
    grouped_data = example_df.groupby('even')
    print(grouped_data['value'].apply(second_largest))

# --- Quiz ---
# DataFrame with cumulative entries and exits for multiple stations
ridership_df = pd.DataFrame({
    'UNIT': ['R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051', 'R079', 'R051'],
    'TIMEn': ['00:00:00', '02:00:00', '04:00:00', '06:00:00', '08:00:00', '10:00:00', '12:00:00', '14:00:00', '16:00:00'],
    'ENTRIESn': [3144312, 8936644, 3144335, 8936658, 3144353, 8936687, 3144424, 8936819, 3144594],
    'EXITSn': [1088151, 13755385,  1088159, 13755393,  1088177, 13755598, 1088231, 13756191,  1088275]
})

def get_hourly_entries_and_exits(entries_and_exits):
    '''
    Fill in this function to take a DataFrame with cumulative entries
    and exits and return a DataFrame with hourly entries and exits.
    The hourly entries and exits should be calculated separately for
    each station (the 'UNIT' column).

    Hint: Take a look at the `get_hourly_entries_and_exits()` function
    you wrote in a previous quiz, DataFrame Vectorized Operations. If
    you copy it here and rename it, you can use it and the `.apply()`
    function to help solve this problem.
    '''
    return entries_and_exits - entries_and_exits.shift(1)
    # 使用之前的shift方法

print(ridership_df.groupby('UNIT')['ENTRIESn', 'EXITSn'].apply(get_hourly_entries_and_exits))
# 按照UNIT进行分组，并调用函数计算每小时的值
# 注意如果不指定对['ENTRIESn', 'EXITSn']做操作的话会报错
# 因为其他列包含数值，使用.apply()会报错的
