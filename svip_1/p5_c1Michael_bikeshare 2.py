import time
import pandas as pd
import numpy as np



CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    cities = CITY_DATA.keys()
    city = input_mod('Which city do you want to explore? ...\n',
              'Sorry, please input a city name among... :\n',
              ['Chicago', 'New York City', 'Washington'])
	# TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    months = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
    month = input_mod('which month to check ? January, February, March, April, May, June or All\n'
        ,'sorry! Please input correct month: \n'
        ,months)
    days = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = input_mod('what day to check? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All\n'
        ,'Sorry! Please input correct day: \n'
        ,days)

	

    print('-'*40)
    return city, month, day



def input_mod(input_print,error_print,enterable_list):


	ret = input(input_print).title()
	while ret not in enterable_list:

		ret = input(error_print).title()
	return ret    	
	
	

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

    # filter by month if applicable

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    # filter by day of week if applicable

        df = df[df['month'] == month]
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    the_most_month = df['month'].mode()[0]
    print('The most common month: ', the_most_month)

    # TO DO: display the most common day of week
    the_most_week = df['day_of_week'].mode()[0]
    print('The most common day of week: ', the_most_week)

    # TO DO: display the most common start hour
    the_most_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour: ', the_most_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    the_most_start_station = df['Start Station'].mode()[0]
    print('The most common start station: ', the_most_start_station)

    # TO DO: display most commonly used end station
    the_most_end_station = df['End Station'].mode()[0]
    print('The most common end station: ', the_most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['popular_station'] = df['Start Station']+'->'+df['End Station']
    #popular_station = df[df['popular_station']].mode()
    popular_station = df['popular_station'].mode()[0]
    print('The frequent combination: ',popular_station)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User type: ',user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
    	print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
    	earliest = df['Birth Year'].min()
    	print('Earliest of birth: ',earliest)
    	recent = df['Birth Year'].max()
    	print('Recent of birth: ',recent)
    	common = df['Birth Year'].mode()
    	print('Common of birth: ',common)
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
