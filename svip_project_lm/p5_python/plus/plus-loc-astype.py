import pandas as pd

df = pd.read_csv('chicago.csv')
print(df.info())
df['Start Time'] = pd.to_datetime(df['Start Time'])

# datatime无法通过匹配过滤，要转换成str
df['day'] = df['Start Time'].dt.date.astype('str')
print(df.info())
print(df.head())
date = df.loc[df['Start Time'].dt.date == '2017-06-23']
print(date.shape)


filter1 = df[df['day'] == '2017-06-23']
print(filter1)