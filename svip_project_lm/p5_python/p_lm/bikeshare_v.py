import time
import pandas as pd
filename = 'chicago.csv'

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
    city = input ('Q1: Chicago, new york city and washington, Which city would you like to explore?').lower()
    while city not in ['chicago', 'new york city', 'washington']:
        city = input('Sorry, please choose one city from chicago, new york city and washington.').lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    mon_option = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = ''
    while month not in mon_option:   
        month = input ('Q2: which month do you want to explore? choose from all, january, february, ... , june. >')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month                  
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_option = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:  
        day = input ('Q3: which day do you want to explore? choose from all, monday, tuesday, ... , sunday. >')               
    if day in day_option:
        break
    else:
        print('---warning: I do not have data about that day.\n---Or you type a wrong name\n---Input Again')
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
    if month != 'all':
        month_option = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month_int]
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day!= 'all':
        day_option = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_int = day_option.index(day) + 1 
        df = df[df['day_of_week'] == day_title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day                 
    most_common_day = df['day'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('most freq month is:')
    print(most_common_month)                    
    print('most freq day in a week is:')
    print(most_common_day)
    print('most freq hour is:')
    print(most_common_hour)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station                       
    commonly_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    top = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start station and end station trip is {} to {}".format(top[0], top[1]))
    
                             
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('most freq start station is:')
    print(commonly_start_station)
    print('most freq end station is:')
    print(commonly_end_station)     
                               
                                  


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
    print('total trip time is:')
    print(total_trip_time)
    print('mean trip time is:')
    print(total_trip_time)                              

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()
    
            
       
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    recent = df['Birth Year'].max()
    common = df['Birth Year'].mode()[0]
   
   #get gender info and print
    try:
        gender_types = df['Gender'].value_counts()
    except KeyError:
        print('>>>The city you choose do not have /Gender/ data:')
    else:
        print('\n>>>gender types is:')
    print(gender_types)
   
   
    #get birth year info and print
    try:
        birth_year = df['Birth Year'].value_counts()
    except KeyError:
        print('>>>The birth year you choose do not have /Birth Year/ data:')
    else:
        print('\n>>>birht year is:')
    print(birth_year)
 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('user types is:')
    print(user_types)
    print('gender types is:')
    print(gender_types)
    print('earliset year of birth is:')
    print(earliest)
    print('recent year of birth is:')
    print(recent)
    print('common year of birth is:')
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
