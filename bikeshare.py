# Branch Master
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

    # To do: Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ''

    while True:

        print("\n Please choose a city any!!!!")

        print("\n 1. Chicago | 2. New York City | 3. Washington\n")

        city = input().lower()

        if city not in CITY_DATA.keys():

            print("\n Please choose again!")

        else:

            break

    print("\nYou have chosen city {}".format(city.title()))



    # To do: Get user input for month (all, january, february, ... , june)

    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}

    month = ''

    while month not in MONTH_DATA.keys():

        print("\nPlease enter the month, between January to June:")

        print("\n(You may also view data for all months, please type 'all'.)\n")

        month = input().lower()

        if month not in MONTH_DATA.keys():

            print("\nInvalid input. Please try again between January to June")

    print(f"\nYou have chosen month {month.title()}")



    # To do: Get user input for day of week (all, monday, tuesday, ... sunday)

    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    day = ''

    while day not in DAY_LIST:

        print("\nPlease enter a day in the week:")

        print("\n(You can also put 'all' or 'All' to view data for all days in a week.)\n")

        day = input().lower()

        if day not in DAY_LIST:

            print("\nInvalid input. Please try again days")

    print(f"\nYou have chosen {day.title()}.")

    print(f"\nYou have chosen to view data for city: {city.upper()}, month/s: {month.upper()} and day/s: {day.upper()}.")

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



    # Convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name



    # Filter by day of week and month

    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1

        df = df[df['month'] == month]

    return df



def time_stats(df):

    """Displays statistics on the most frequent times of travel."""



    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()



    # display the most common month

    popular_month = df['month'].mode()[0]

    print(f"The most common month (1 = January,...,6 = June): {popular_month}")



    # display the most common day of week

    popular_day = df['day_of_week'].mode()[0]

    print(f"\nThe most common day of week: {popular_day}")

 

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]

    print(f"\nThe most common start hour: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)



def station_stats(df):

    """Displays statistics on the most popular stations and trip."""



    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

 

    # display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]

    print(f"The most commonly used start station: {common_start_station}")



    # display most commonly used end station

    common_end_station = df['End Station'].mode()[0]

    print(f"\nThe most commonly used end station: {common_end_station}")



    # display most frequent combination of start station and end station trip

    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')

    combo = df['Start To End'].mode()[0]

 

    print(f"\nThe most frequent combination of trips are from {combo}.")

 

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)



def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""



    print('\nCalculating Trip Duration...\n')

    start_time = time.time()



    # display total travel time

    total_duration = df['Trip Duration'].sum()

    minute, second = divmod(total_duration, 60)

    hour, minute = divmod(minute, 60)

    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")



    # display mean travel time

    average_duration = round(df['Trip Duration'].mean())

    mins, sec = divmod(average_duration, 60)

    if mins > 60:

        hrs, mins = divmod(mins, 60)

        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")

    else:

        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")



    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)



def user_stats(df):

    """Displays statistics on bikeshare users."""



    print('\nCalculating User Stats...\n')

    start_time = time.time()



    # Display counts of user types

    user_type = df['User Type'].value_counts()

    print(f"The types of users by number are given below:\n\n{user_type}")



    # Display counts of gender

    try:

        gender = df['Gender'].value_counts()

        print(f"\nThe types of users by gender are given below:\n\n{gender}")

    except:

        print("\nThere is no 'Gender' column in this file.")



    # Display earliest, most recent, and most common year of birth

    try:

        earliest = int(df['Birth Year'].min())

        recent = int(df['Birth Year'].max())

        common_year = int(df['Birth Year'].mode()[0])

        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")

    except:

        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)



# Function to display the data frame itself as per user request

def display_data(df):

    """Displays 5 rows of data from the csv file for the selected city.

    Args:

        param1 (df): The data frame you wish to work with.

    Returns:

        None.

    """

    BIN_RESPONSE_LIST = ['yes', 'no']

    view_data = ''



    # counter variable is initialized

    start_loc = 0

    while view_data not in BIN_RESPONSE_LIST:

        print("\nDo you wish to view the raw data? (yes/no)")

        view_data = input().lower()

        if view_data == "yes":

            print(df.head())

        elif view_data not in BIN_RESPONSE_LIST:

            print("\nPlease check your input.")

 

    #Extra while loop here to ask user if they want to continue viewing data

    while view_data == 'yes':

        start_loc += 5

        view_data = input("Do you wish to continue? (yes/no): ").lower()

        if view_data == "yes":

             print(df[start_loc:start_loc+5])

        elif view_data != "yes":

             break

    print('-'*80)

 



def main():

    while True:

        city, month, day = get_filters()

        df = load_data(city, month, day)

        display_data(df)

        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':

            break



if __name__ == "__main__":

    main()