import pandas as pd

filename = 'nyc-subway-weather.csv'
subway_df = pd.read_csv(filename)

def correlation(x, y):
    '''
    Fill in this function to compute the correlation between the two
    input variables. Each input is either a NumPy array or a Pandas
    Series.

    correlation = average of (x in standard units) times (y in standard units)

    Remember to pass the argument "ddof=0" to the Pandas std() function!
    '''
    std_x = (x - x.mean()) / x.std(ddof=0)
    std_y = (y - y.mean()) / y.std(ddof=0)
    # 将x，y做标准化（见之前的知识）

    return (std_x * std_y).mean()
    # 返回r相关性指标

entries = subway_df['ENTRIESn_hourly']
cum_entries = subway_df['ENTRIESn']
rain = subway_df['meanprecipi']
temp = subway_df['meantempi']

#print(subway_df)

print (correlation(entries, rain))
print (correlation(entries, temp))
print (correlation(rain, temp))

print (correlation(entries, cum_entries))
