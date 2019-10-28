import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Pre-defined variables to be selected by user

CITIES = ['chicago', 'new york city', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

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
    while True:
       city = input('Which city do you want to explore Chicago, New York city or Washington?\n> ').lower()
       if city in CITIES:
            print(city.title() + ' was selected as a city')   
            break
       else:
            print('invalid input')
    
    # TO DO: get user input for month (all, january, february, ... , june) and make sure it's lower case
    while True:
        month = input('Which month are you interested in?\n> ').lower()
        if month in MONTHS:
            print(month.title() + ' was selected as a month')
            break
        else:
            print('invalid input')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which week day do you want to analyze?\n> ').lower()
        if day in DAYS:
            print(day.title() + ' was selected as a day')
            break
        else:
            print('invalid input')

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    df['start-end st.'] = df['Start Station'] + ' - ' + df['End Station']
    # filter by month if applicable
    if month != 'all':
        df = df[ df['month'] == month.title() ]
       
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()
    print("The most common month is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()
    print("The most common day of week is :", most_common_day_of_week)

    # TO DO: display the most common start hour
    most_common_start_hour = df['hour'].mode()
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()
    print("The most commonly used start station :", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print("The most commonly used end station :", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_station_combo = df['start-end st.'].mode()
    print("The most frequent combination of start station and end station trip:", most_common_station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of User Types:\n", user_type_counts)

    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        df['Gender'] = 'Not known'
    if 'Birth Year' not in df.columns:
        df['Birth Year'] = 0
    gender_counts = df['Gender'].value_counts()
    print("Counts of gender:\n", gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    min_yob = df['Birth Year'].min()
    max_yob = df['Birth Year'].max()
    mode_yob = df['Birth Year'].mode()
    print("Min year of birth:\n", min_yob)
    print("Max year of birth:\n", max_yob)
    print("Most common year of birth:\n", mode_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def raw_data(df):
    """Display raw data as per user request"""

    start_loc = 0
    end_loc = 5

    display_raw = input("Would you like to see raw data?: ").lower()

    if display_raw == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Would you like to see next 5 rows?:\n").lower()
            if end_display != 'yes':
                break

                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
