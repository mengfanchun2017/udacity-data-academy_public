import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_values = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
week_values = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n'+'#### Hello! Let\'s explore some US bikeshare data! ####')
    print('\n' + '-'* 15 + 'Step 1 : Select data' + '-'* 15)
    '''
    创建一个用于控制输入的函数，输入用于获取打印、错误返回、参数范围、获取的参数，返回需要分析的city、month、weekday。
    判别输入的值在参数范围中，打印并返回输入的参数，不在范围中，返回错误值，或者跳出。
    '''
    def input_mod(input_print, error_print, enterable_list, get_value):
        while True:
            ret = input(input_print)
            ret = get_value(ret) #这里执行作为参数的函数
            if ret in enterable_list:
                print('You have selected {}.'.format(ret.title()))
                return ret
            else:
                print(error_print)

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input_mod('\n****Which city would you like to see data from? \n****Choice from <Chicago, New york city, Washington>' \
                     '\n>>>>',
                     '\n****Error!Please select city from Chicago, New york city, Washington!  Or press Ctrl+C to end this program.****',
                     CITY_DATA.keys(),
                     lambda x: str.lower(x))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input_mod('\n****Which month would you like to see?****'\
                      '\n****Input \'all\' to apply no month filter, or select from <January, Fabruary, March, April, May, June>'\
                      '\n>>>>',
                      '\n****Error!Please imput a correct month name! Or press Ctrl+C to end this program.****',
                      month_values,
                      lambda x: str.lower(x))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_mod('\n****Which day in the week would you like to see?****'\
                    '\n****Imput \'all\' to apply no day filter, or select any day in the week, like Monday, Thursday ......'\
                    '\n>>>>',
                    '\n****Error!Please imput a correct the day of the week! Or press Ctrl+C to end this program.****',
                    week_values,
                    lambda x: str.lower(x))

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
    print('\n>>>>>>>>>Got Inputs:>>>>>>>>>>')
    print('>>>>City requirement: {}'.format(city.title()))
    print('>>>>Month requirement: {}'.format(month.title()))
    print('>>>>Day requirement: {}'.format(day.title()))
    print('\n' + '-'* 15 + 'Step 2 : Calculating data' + '-'* 15)

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # add two new columns: month column and day of week column from Start Time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\n......Calculating The Most Frequent Times of Travel......\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('>>>>The most common month is : \n>>>>{}.'.format(month_values[most_common_month - 1].title()))

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('>>>>The most common day of week is : \n>>>>{}.'.format(most_common_day_of_week))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('>>>>The most common start hour is : \n>>>>{}.'.format(most_common_start_hour))

    print("\n****This took %s seconds.****" % (time.time() - start_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n......Calculating The Most Popular Stations and Trip......\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('>>>>The most commonly used start station is : \n>>>>{}.'.format(most_commonly_used_start_station))

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('>>>>The most commonly used end station is : \n>>>>{}.'.format(most_commonly_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    #Modified as reviewed

    top = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('>>>>The most frequent combination of start station and end station trip is:\n>>>>' \
          '{} to {}.'.format(top[0], top[1]))

    print("\n****This took %s seconds.****" % (time.time() - start_time))


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n......Calculating Trip Duration......\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('>>>>The total travel time is : \n>>>>{}.'.format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('>>>>The mean travel time is : \n>>>>{}.'.format(mean_travel_time))
    #display max travel time
    max_travel_time = df['Trip Duration'].max()
    print('>>>>The maximum travel time is : \n>>>>{}.'.format(max_travel_time))
    #display min travel time
    min_travel_time = df['Trip Duration'].min()
    print('>>>>The minimum travel time is : \n>>>>{}.'.format(min_travel_time))

    print("\n****This took %s seconds.****" % (time.time() - start_time))


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n......Calculating User Stats......\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        print('>>>>The counts of user types is: \n{}\n'.format(df['User Type'].value_counts()))
    except KeyError:
        print('>>>>There is no User Type data in this city')#错误处理

    # TO DO: Display counts of gender
    try:
        print('>>>>The counts of user gender is: \n{}\n'.format(df['Gender'].value_counts()))
    except KeyError:
        print('>>>>There is no Gender data in this city!')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        most_recent_year_of_birth = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print('>>>>The earliest year of birth is: \n>>>>{} \
                \n>>>>The most recent is: \n>>>>{} \
                \n>>>>The most common is: \n>>>>{}'\
                    .format(earliest_year_of_birth, most_recent_year_of_birth, most_common_year_of_birth))
    except KeyError:
        print('>>>>There is no Birth Year in this city')#错误处理

    print("\n****This took %s seconds.****" % (time.time() - start_time))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n>>>>Would you like to restart? \n>>>>Enter yes to restart or any key to quit.\n>>>>')
        if restart.lower() != 'yes':
            print('>>>>Bye~')
            break


if __name__ == "__main__":
	main()
