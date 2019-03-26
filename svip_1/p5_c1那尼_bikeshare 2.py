import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def input_mod(input_print,error_print,enterable_list):
    ret = input(input_print).lower()
    while ret not in enterable_list:
        ret = input(error_print).lower()
    return ret


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
    city = input_mod('Would you like to see data for Chicago, New York City, or Washington?\n',
                'Error!Please input the correct city name: ',
                CITY_DATA.keys())
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input_mod('Which month? All, January, February, March, April, May,or June?\n',
                'Error!Please input the correct month name: ',
                ['all', 'january', 'february', 'march', 'april', 'may', 'june'])
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input_mod('Which day? All, Monday, Tuesday, ... Sunday?\n',
                'Error!Please input the correct weekday name: ',
                ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])

    print('-'*80)
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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
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

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print('What was the most frequent times of travel?')
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month: ', common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day: ', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most common start hour: ', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    print('Below are the most popular start and end station respectively.')
    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Start station: ', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('End station: ', popular_end_station)
    print()
    # TO DO: display most frequent combination of start station and end station trip
    top = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip :\n {} to {}".format(top[0], top[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('What is the breakdown of the users?\n', user_type)
    print()
    try:
    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print('What is the breakdown of gender?\n', gender)
        print()
    # TO DO: Display earliest, most recent, and most common year of birth
        print('what is the earliest, most recent, and most common year of birth?')
        min_birth = int(df['Birth Year'].min())
        max_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode())
        print('Earliest year of birth: ', min_birth)
        print('Most recent year of birth: ', max_birth)
        print('Most common year of birth: ', common_birth)
    except:
        print('Error: missing data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,month):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    print('What was the total travel time for 2017 through {}, and waht was the average time spend on each trip?'.format(month))
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ',total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time: ', mean_travel_time)
    print()
    trip_detail = input('would you want to know more detail statistics about trip duation? Enter yes or no.\n')
    if trip_detail == 'yes':
        print('Detail statistics:\n', df['Trip Duration'].describe())
    elif trip_detail == 'no':
        print()
    else:
        print('Sorry, invalid input. Enter again: ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        user_stats(df,city)
        trip_duration_stats(df,month)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
