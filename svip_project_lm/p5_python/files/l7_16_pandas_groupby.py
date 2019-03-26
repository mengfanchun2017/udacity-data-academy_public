import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Change False to True for each block of code to see what it does

# Examine DataFrame
if 0:
    print (example_df)

# Examine groups
if 0:
    grouped_data = example_df.groupby('even')
    # The groups attribute is a dictionary mapping keys to lists of row indexes
    print (grouped_data.groups)
    #会按照False和True进行拆分

# Group by multiple columns
if 0:
    grouped_data = example_df.groupby(['even', 'above_three'])
    print (grouped_data.groups)
    #会按照两个groupby的组合进行拆分，注意愿数据中没有True，False这种，所以结果是3种

# Get sum of each group
if 0:
    grouped_data = example_df.groupby('even')
    print (grouped_data.sum())
    #这里会按照groupby even拆分出两组，并分别计算sum（value的求和）

# Limit columns in result
if 0:
    grouped_data = example_df.groupby('even')

    # You can take one or more columns from the result DataFrame
    print (grouped_data.sum()['value'])

    print ('\n') # Blank line to separate results

    # You can also take a subset of columns from the grouped data before
    # collapsing to a DataFrame. In this case, the result is the same.
    print (grouped_data['value'].sum())

filename = 'nyc-subway-weather.csv'
subway_df = pd.read_csv(filename)
#print(subway_df.head())
### Write code here to group the subway data by a variable of your choice, then
### either print out the mean ridership within each group or create a plot.
#print(subway_df.groupby('day_week').mean())

print(subway_df.groupby('day_week').mean()['ENTRIESn_hourly'])
