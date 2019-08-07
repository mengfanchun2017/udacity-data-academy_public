import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters_arc():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # archive version of get_filters
    ## do not use phase_input fuction to solve repetition

    # 这里的 city_option 可以进行简化
    # 因为前面的 CITY_DATA 是字典结构，可以通过 .keys() 直接输出字典的名字
    # 旧的方法：city_option = ['chicago', 'new york city', 'washington']
    # 新的方法：
    city_option = CITY_DATA.keys()
    
    mon_option = ['all', 'january', 'february', 'march', 'april', 'may', 
                  'june']
    day_option = ['all', 'monday', 'tuesday',  'wednesday', 
                  'thursday', 'friday', 'saturday', 'sunday' ]
    #三个输入的备选
    
    while True:
        city = input('q1/3: which city do you want to know? \
                     \noption:<chicago,new york city,washington> \n>>> ')
        # 在input中如果加入了\换行符会在输出中换行，保持不换行会突破79个字符，怎么解
        # 这里在第二行前增加了\n用两行输出了
        if city in city_option:
            break
        else:
            print('---warning: I do not have data about that city.\
                  \n---Or you type a wrong name\n---Input Again')
    #要求输入city并检查是否合法

    while True:
    # 总是循环执行，直到遇到break
        month = input('q2/3: which month do you want to know? \
                      \noption:<all,january,february,march,april,may,june>\
                      \n>>> ')
        # \ 是代码换行的意思，python的编程规范是每行不超过79个字符
        if month in mon_option:
            break
        else:
            print('---warning: I do not have data about that month.\n---Or you type a wrong name\n---Input Again')
    # 当经过判断 month 变量在可选范围内，就break结束while循环

    while True:
        day = input('q3/3: which day do you want to know? \
                    \noption:<all,monday,tuesday,wednesday, ... ,sunday>\
                    \n>>> ')
        if day in day_option:
            break
        else:
            print('---warning: I do not have data about that day.\
                  \n---Or you type a wrong name\n---Input Again')
    
    # 为了提高用户体验，输出下刚刚收集到的3个变量
    str_got_input = 'Got Inputs:'
    print('')
    print(str_got_input.center(30,'>'))
    #str有.ljust .center .rjust等方式不使用变量的话很方便
    #http://www.tutorialspoint.com/python/string_ljust.htm

    print('>>>city requirement:',city)
    print('>>>month requirement:',month)
    print('>>>day requirement:',day)
    
    return city, month, day

## get filter update start
### get filter - sige function

def phrase_input(input_prompt,err_prompt,option_list):
    # old version
    ## user_input = input(input_prompt).lower()
    ## while user_input not in option_list:
    ##     user_input = input(err_prompt)
    while True:
        user_input = input(input_prompt).lower()
        if user_input in option_list:
            return user_input
    # lower 是将用户的输入转换为小写，这样只要内容对了，第一个字母大写也可以通过
    
def get_filters():
    
    city_option = CITY_DATA.keys()
    month_option = ['all', 'january', 'february', 'march', 'april', 'may', 
                  'june']
    day_option = ['all', 'monday', 'tuesday',  'wednesday', 
                  'thursday', 'friday', 'saturday', 'sunday' ]
    
    #将city、month、day、err的输出分离出来
    city_prompt = 'q1/3: which city do you want to know? \
                     \noption:<chicago,new york city,washington> \n>>> '
    month_prompt = 'q2/3: which month do you want to know? \
                      \noption:<all,january,february,march,april,may,june>\
                      \n>>> '
    day_prompt = 'q3/3: which day do you want to know? \
                    \noption:<all,monday,tuesday,wednesday, ... ,sunday>\
                    \n>>> '
    err_prompt = '---warning: I do not have that data.\
                  \n---Or you type a wrong name\n---Input Again\n>>> '
    
    #调用3次函数，将结果赋值给city、month、day三个变量                 
    city = phrase_input(city_prompt,err_prompt,city_option)
    month = phrase_input(month_prompt,err_prompt,month_option)
    day = phrase_input(day_prompt,err_prompt,day_option)
    
    #为了提高用户体验，输出下刚刚收集到的3个变量
    str_got_input = 'Got Inputs:'
    print('')
    print(str_got_input.center(30,'>'))
    #str有.ljust .center .rjust等方式不使用变量的话很方便
    #http://www.tutorialspoint.com/python/string_ljust.htm
    print('>>>city requirement:',city)
    print('>>>month requirement:',month)
    print('>>>day requirement:',day)
    
    return city, month, day

## get filter update end


def load_data(city, month, day):
# 定义函数，根据用户输入的3个变量处理数据
# city是要处理那个城市
# month、day是要处理的月份和天输入

    df = pd.read_csv(CITY_DATA[city])
    # 根据输入的city读入csv文件

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # 将时间从字符格式转为datetime格式

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # 将month和weekday抽离出来建立新的列
    # 是为了后面根据输入进行数据筛选时候的参考

    if month != 'all':
    # 如果月份要求不是all，则按照要求筛选数据

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # 这是可选的所有月份
        month = months.index(month) + 1
        # 定义month变量等于输入月份的索引加1
        # 为什么要加1呢？
        # 因为索引是从0开始，用户输入是从1开始

        df = df[df['month'] == month]
        # 最后对df做更新
        # 右边df['month'] == month是一种过滤
        # 左边是month列的所有内容（1-6月）
        # 右边是刚刚生成的要筛选的month变量（由用户输入）
        # 中间是判断是否相等 ==
        # 结果就是满足右边条件的数据被重新写入df里
        # 如果 month = all，则不会运行这个过滤

    if day != 'all':
    # day的筛选方式同上
        df = df[df['day_of_week'] == day.title()]
        # 使用用 day.title() 讲日期输入的小写变成首字母大写
        # 比如输入的 day 是 january，就会变为 January
        # 而 ’day_of_week' 是前面用 dt.weekday_name 抽出的
        # 抽出之后就是首字母大写的
        # 这样前后就对应上了

    return df


def time_stats(df):
    print('\n...Calculating The Most Frequent Times of Travel...\n')
    # 先是打印一行提示
    start_time = time.time()
    # 此处可以忽略，是调用time函数用于计算代码的执行时间

    # 为了能够计算时间要变换为pandas里面的时间格式
    # 就是使用.to_datetime()这个方法转换格式
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    max_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    max_day = df['day'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    max_hour = df['hour'].mode()[0]

    print("(Took %s seconds.)" % (time.time() - start_time))
    # 后面的time.time() - start_time就是用当前时间剪去开始运行时的时间
    # 可以看出这段代码运行了多长时间
    
    print('>>>max freq month is: ',max_month)
    print('>>>max freq day is: ',max_day)
    print('>>>max freq hour is: ',max_hour)
    #以上是3个频率的输出


def station_stats_arc(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n...Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    max_startsta = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    max_endsta = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    # 问题3是问那个车站组合出现最多
    # 为了回答这个问题，我们可以在数据新建1列
    # 例子命名为combine_sation
    # 由Start Station的数据加上End Station合并
    # 为了便于识别，我加上了 - - - 作为标签
    # 再之后就一样是使用mode()进行统计了
    df['combine_station'] = df['Start Station'] + ' --- ' + df['End Station']
    max_combine = df['combine_station'].mode()[0]

    print("(This took %s seconds.)" % (time.time() - start_time))

    print('>>>max freq start station is:')
    print(max_startsta)
    print('\n>>>max freq end station is:')
    print(max_endsta)
    print('\n>>>max freq combine statuion is:')
    print(max_combine)
    #以上是3个频率的输出
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n...Calculating The Most Popular Stations and Trip (groupby methord)...\n')
    start_time = time.time()
    
    # 以下为使用groupby解决问题
    station_orderd_two = df.groupby(['Start Station', 'End Station']).size().idxmax()
    ## groupby 输入了两个参数 ['Start Station', 'End Station']，注意要放到[]中以列表形式输入
    ## 那么结果就会先统计 start station，再统计 end station
    ## size 的意思是求上面输出的数量(转换为int整数)
    ## idxmax 的意思是说把 size 输出的整数，最大的挑出来
    ### 这里注意输出是没有排序的（也不用排序，计算量大）使用 idxmax 就能发现最大的
    ### 因为 groupby 是两个，所以输出也是一个列表
    
    print(df.groupby(['Start Station', 'End Station']))
    print(df.groupby(['Start Station', 'End Station']).size())
    print(df.groupby(['Start Station', 'End Station']).size().idxmax())
    
    print('\n>>>max freq combine statuion is:\n {} -----> {}'
          .format(station_orderd_two[0], station_orderd_two[1]))
    ## 所以这里可以用[0]、[1]分别代表最多组合中的 start station ，和 end station
    
    print("(This took %s seconds.)" % (time.time() - start_time))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n...Calculating Trip Duration...\n')
    start_time = time.time()

    # 使用.sum()方法求和
    total_trip_time = df['Trip Duration'].sum()

    # 使用.mean()方法求平均值
    mean_trip_time = df['Trip Duration'].mean()


    print("(Took %s seconds.)" % (time.time() - start_time))
    print('>>>total trip time is:')
    print(total_trip_time)
    print('>>>mean trip time is:')
    print(mean_trip_time)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n...Calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # 使用.
    user_types = df['User Type'].value_counts()
    print('>>>user types is:')
    print(user_types)
    
    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
    except KeyError:
        print('>>>The city you choose do not have /Gender/ data:')
    else:
        print('\n>>>gender types is:')
        print(gender_types)
    finally:
        pass
    # 也可以使用 ’Gender‘ in df.columns 做循环判断，这种方法不适用于try/except
    # 因为不会报错

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
    except KeyError:
        print('>>>The city you choose do not have /Year/ data:')
    else:
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        print('\n>>>earliest year of birth is:')
        print(int(earliest))
        print('\n>>>recent year of birth is:')
        print(int(recent))
        print('\n>>>common year of birth is:')
        print(int(common))
    finally:
        pass

    print("(Took %s seconds.)" % (time.time() - start_time))

def main():
    while True:
        
        str_title = 'Hello! Let\'s explore some US bikeshare data!'
        print(str_title.center(48,'#'))
        print('')
        
        str_input = 'Step1 : Get input'
        print(str_input.center(48,'-'))
        
        #city, month, day = get_filters()
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        str_input = 'Step2 : Computing'
        print('')
        print(str_input.center(48,'-'))
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n### Proceeding complete. \
                        \n### Would you like to restart? \
                        \n### Enter yes to restart or any key to quit.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
