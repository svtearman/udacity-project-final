import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = { 'january' : 1,
                  'february' : 2,
                  'march' : 3,
                  'april' : 4,
                  'may' : 5,
                  'june' : 6,
                  'all' : '1, 2, 3, 4, 5, 6' }

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
    print('What city would you like to explore? (Chicago, New York City, Washington)')
    #gets user input for city
    city = input('City Name: ').lower()
    if city in CITY_DATA:
         print('You have choosen: ' + city)
    else:
        city = 'chicago'
        print('That city is not on our list, so we have redirected you to show you our favorite city, Chicago.')
        
    

    # TO DO: get user input for month (all, january, february, ... , june)
    print('What month would you like to pull data from? (January, February, March, April, May, June, or All)')
   
    month = input('Month: ').lower()
    if month in MONTH_DATA:
        print('You have selected: ' + month)
    else:
        month = 'january'
        print('You have selected a month that is unavailable, so we have redirected you to show you our favorite month, Janurary.')
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('What day of the week would you like to pull data from? (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday)')
    day = input('Day: ').lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if day in days:
        print('You have selected: ' + day)
    else:
        day = 'monday'
        print('You have selected a day that is unavailable, so we have redirected you to show you our favorite day, Monday.')
            

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
    #loads data from specific times
    df = pd.read_csv(CITY_DATA[city])
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
    #sets up to use datetime functions
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    # translate numeric month to text
    key_list = list(MONTH_DATA.keys())
    val_list = list(MONTH_DATA.values())
    print('The most popular month is: ')
    print(key_list[val_list.index(popular_month)])
   
    

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most popular day of the week is: ')
    print(popular_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour is: ')
    print(popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    max_start_station = df['Start Station'].describe()["top"]   
    print('The most common start station is: ')
    print(max_start_station)

    
    # TO DO: display most commonly used end station
    max_end_station = df['End Station'].describe()["top"]
    print('The most common end station is: ')
    print(max_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combo_station = df.groupby(['Start Station','End Station']).size().idxmax()
    print('The most common combination of start and end station is: ')
    print(combo_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #gets sum of trip duration to get total travel time
    sum_trip = df['Trip Duration'].sum() 
    print('The total travel time is: ')
    print(sum_trip)

    # TO DO: display mean travel time
    mean_trip = df['Trip Duration'].mean()
    print('The mean travel time is: ')
    print(mean_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User type counts: ')
    print(user_types)

    # TO DO: Display counts of gender
    #uses try and except to not get an error for washington which does not have gender data
    try:
        gender_set = df['Gender'].value_counts()
        
        
    except:
        gender_set = 'No Gender Data Available'
        
    
    print('Gender type counts: ')
    print(gender_set)

    # TO DO: Display earliest, most recent, and most common year of birth
    #uses try and except to not get an error because washington does not have birth year data
    try:
        earliest_birthday = min(df['Birth Year'])
        most_recent_birthday = max(df['Birth Year'])
        top_birthday = df['Birth Year'].value_counts().head(1)
        
        
    except:
        earliest_birthday = 'No birthday data available'
        most_recent_birthday = 'No birthday data available'
        top_birthday = 'No birthday data available'
        
        
    #prints each data set individual so the output is easier to read
    print('The earliest birth year is: ')
    print(earliest_birthday)
    print('The most recent birth year is: ')
    print(most_recent_birthday)
    print('The most common birth year and amount occurred is: ')
    print(top_birthday)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def raw_data_option(df):
    """Displays option to see five lines of raw data."""
    df = pd.read_csv(CITY_DATA[city])
    print('Would you like to see five lines off raw data?')
    answer = input('Yes or No: ').lower()
    answers = ['yes', 'no']
    #uses if and else to handle any misspelling on the user's end to prevent errors
    #for answer in answers: 
        #print(row1 = CITY_DATA[city].iloc[5])
        #if answer == 'no': 
            #break
        #else:
           # print('Invalid answer, please reset to try again')
    if answer in answers:
        print('You have selected: ' + answer)
        print(df.head(5))
   # if answer == yes:
        #answer = 'yes'
       # print(row1 = data.iloc[5]
   # else:
       # answer = no
        #answer = 'no'
       # print('You have selected "no", if you change your mind, please restart to try again.')
        #break
    else:
        answer = 'yes'
        print(df.head(5))
        print('You have selected an answer that is unavailable, so we have redirected you to automatically show you five lines of raw data.')
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data_option(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
