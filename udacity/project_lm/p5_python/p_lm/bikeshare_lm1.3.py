wimport time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city_option = ['chicago', 'new york city', 'washington']
    mon_option = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    day_option = ['all', 'monday', 'tuesday',  'wednesday', 'thursday', 'friday', 'saturday', 'sunday' ]
    #三个输入的备选

    while True:
        city = input('q1/3: which city do you want to know? chicago, new york city or washington? > ')
        if city in city_option:
            break
    #要求输入city并检查是否合法

    while True:
    # 总是循环执行，直到遇到break
        month = input('q2/3: which month do you want to know? choose from all, \
                  january, february, ... , june. > ')
        # \ 是代码换行的意思，python的编程规范是每行不超过79个字符
        if month in mon_option:
            break
    # 当经过判断 month 变量在可选范围内，就break结束while循环

    while True:
        day = input('q3/3: which day do you want to know? choose from all, \
                  monday, ... , sunday. > ')
        if day in day_option:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
       
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
    df = df[df['month'] == month]
    
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    max_month = df['month'].mode()[0]
    
    df['day'] = df['Start Time'].dt.day
    max_day = df['day'].mode()[0]
    
    df['hour'] = df['Start Time'].dt.hour
    max_hour = df['hour'].mode()[0]
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    print('\noriginal time: ')
    print(df['Start Time'].head())
    print(df['month'].head())
    popular_month = df['month'].mode()[0]
    print('\n(pretty) Most Popular Start month:', popular_month)
    print("\nThis took %s seconds." % (time.time() - start_time))

    # TO DO: display the most common day of week
    df['week'] = df['Start Time'].dt.week
    print('\noriginal time: ')
    print(df['Start Time'].head())
    print('\nonly week: ')
    print(df['week'].head())
    popular_week = df['week'].mode()[0]
    print('\n(pretty) Most Popular Start week:', popular_week)
    print("\nThis took %s seconds." % (time.time() - start_time))
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('\noriginal time: ')
    print(df['Start Time'].head())
    print('\nonly hour: ')
    print(df['hour'].head())
    
    popular_hour = df['hour'].mode()[0]
    print('\n(pretty) Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df = pd.read_csv(CITY_DATA[city])
    # TO DO: display most commonly used start station
    

    # TO DO: display most commonly used end station
    df['combine_station'] = df['Start Station'] + ' --- ' + df['End Station']
    max_combine = df['combine_station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
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

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('max freq start station is:')
    print(max_startsta)
    print('\nmax freq end station is:')
    print(max_endsta)
    print('\nmax freq combine statuion is:')
    print(max_combine)
    #以上是3个频率的输出
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df = pd.read_csv(CITY_DATA[city])
    # TO DO: display total travel time
    total_trip_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_trip_time = df['Trip Duration'].mean()

    print('The total trip duration is:')
    print(total_trip_time)
    print('The average trip duration is:')
    print(mean_trip_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    df = pd.read_csv(CITY_DATA[city])
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user types are as follows:\n' + user_types)

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    try:
        gender_types = df['Gender'].value_counts()
    except KeyError:
        print('There is no such data in the city you choose.')
    else:
        print('The user types are as follows:\n' + gender_types)
    finally:
        pass
   
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    recent = df['Birth Year'].max()
    common = df['Birth Year'].mode()[0]
    
    print('The earliest year of birth is :\n' + int(earliest))
    print('The recent year of birth is :\n' + int(recent))
    print('The common year of birth is :\n' + int(common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
