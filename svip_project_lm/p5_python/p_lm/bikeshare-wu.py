import time
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city_option = ['chicago', 'new york city', 'washington']
    city = ' '
    while True:
        city = input('\nWounld you like to see data for chicago, new york city, or washington? Enter city name.\n')
        if city in city_option:
           break
    # TO DO: get user input for month (all, january, february, ... , june)

    mon_option = ['all', 'January', 'February', 'March',  'April',  'May',  'June',  'July',  'August',  'September', 'October', 'November', 'December']
    mon = ' '
    while True:
        month = input('\nWhich month? all, January, February, March, ... , December?\n')
        if month in mon_option:
           break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_option = [ 'all', 'Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = ' '
    while True:   
       day = input('\nWhich day? All, Monday, Tuesday, ... , Sunday?\n')
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

    city, month, day = get_filters()
    df = load_data(city, month, day)
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    # start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    max_month = df['month'].mode( ) [0]

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day
    max_day = df['day'].mode( ) [0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    max_hour = df['hour'].mode( ) [0]

    #  print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(' max frequent month is: ')
    print(max_month)
    print(' max frequent day is: ')
    print(max_day)
    print(' max frequent hour is: ')
    print(max_hour)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    # start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['start Time'])
    # TO DO: display most commonly used start station
    max_start = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    max_end = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['combine_station'] = df['Start Station'] + ' --- ' + df['End Station']
    max_combine = df['combine_station'].mode()[0]

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print(' max frequent start station is: ')
    print(max_start)
    print(' max frequent end station is: ')
    print(max_end)
    print(' max frequent combine station is: ')
    print(max_combine)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    # start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['start Time'])
    # TO DO: display total travel time
    total_trip_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_trip_time = df['Trip Duration'].mean()

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('total trip time is: ')
    print(total_trip_time)
    print('mean trip time is: ')
    print(mean_trip_time)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    # start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    recent = df['Birth Year'].max()
    common = df['Birth Year'].mode()[0]
   
   #  print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('user types is: ')
    print(user_types)
    print('gender types is: ')
    print(gender_types)
    print('earliest year of birth is: ')
    print(earliest)
    print('recent year of birth is: ')
    print(recent)
    print('common year of birth is: ')
    print(common)

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