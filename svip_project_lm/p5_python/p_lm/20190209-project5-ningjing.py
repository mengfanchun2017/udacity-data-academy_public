# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 21:48:41 2019

@author: ningjing
"""

def phrase_input(input_prompt,option_list):
    
    user_input = input(input_prompt).lower()
    while user_input not in option_list:
        user_input = input(input_prompt).lower()
    return user_input




import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def input_mod(input_print,option_list):
    option_input = input(input_print).lower()
    while True:
        ret = input(input_print).lower()
        if ret in enterable_list:
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
    city_option = CITY_DATA.keys()
    mon_option = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    day_option = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    city_input = input('Q1:which city do you want to know? chicago, new york city, washingtion? >')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month_input = input('Q2: which month do you want to know? all, january, february, ... june? >')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_input = input('Q3: which day do you want to know? all, monday, tuesday, ... sunday? > ')

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
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day !='all':
        df = df[df['day_of_week'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

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

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('max frequent month is:')
    print(max_month)
    print('max frequent day is:')
    print(max_day)
    print('max frequent hour is:')
    print(max_hour)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    max_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    max_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    df['combine_station'] = df['Start Station'] + df['End Station']
    max_combine_station = df['combine_station'].mode()[0]
                                                   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('the most frequent start station is:')
    print(max_start_station)
    print('the most frequent end station is:')
    print(max_end_station)
    print('the most frequent combine station is:')
    print(max_combine_station)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    
    # TO DO: display total travel time
    total_trip_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_trip_time = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('total trip duration is:')
    print(total_trip_time)
    print('mean trip duration is:')
    print(mean_trip_time)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_types = df['Gender'].value_counts()


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earlist_birth = df['Birth Year'].min()
        mostrecent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('user types:')
    print(user_types)
    print('gender types:')
    print(gender_types)
    print('the earlist year of birth is:')
    print(earlist_birth)
    print('the most recent year of birth is:')
    print(mostrecent_birth)
    print('the most common year of birth is:')
    print(common_birth)
    

def main():
    while True:        city, month, day = get_filters()
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

    