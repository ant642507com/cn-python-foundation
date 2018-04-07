import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

"""
 cached CSV data in memory!
 In order to void frequently read data from disk!
"""
CACHED_CITY_DATA = {}

"""
Define Global MONTHs
"""
MONTH_LIST = ["January", "February", "March", "April", 
              "May", "June", "July", "August",
              "September", "Octuber", "November", "December"]

"""
Define Global WEEKDAYs
"""
WEEK_LIST = ["Monday", "Tuesday", "Wednesday", "Thursday",
             "Friday", "Saturday", "Sunday"]

def get_filter_mode():
    '''Asks the user want how to filter data.
    Args:
        none.
    Returns:
        (str) filter mode for filter.
    '''
    
    ret_val = None
    while True:
        time_period = input('\nWould you like to filter the data by month, day, both, or not at'
                        ' all? Type "none" for no time filter.\n')
        if time_period in ["month", "day", "both", "none"]:
            ret_val = time_period
            break
        else:
            print("\nError input! Try Again?")
    return ret_val

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.
    Args:
        none.
    Returns:
        (str) cityname for a city's bikeshare data.
    '''
    ret_city = None
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
        if city in ["Chicago", "New York", "Washington"]:
            ret_city = city
            break
        else:
            print("\nError input! Try Again?")
    return ret_city

def get_month():
    '''Asks the user for a month and returns the specified month.
    Args:
        none.
    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    '''
   
    ret_val = None
    while True:
        month = input('\nWhich month? January, February, March, April, May, or June? (or "all")\n')
        if month in ["all"] + MONTH_LIST:
            ret_val = month
            break
        else:
            print("\nError input! Try Again?")
    return ret_val

def get_day():
    '''Asks the user for a day and returns the specified day.
    Args:
        none.
    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    '''
    ret_val = None
    while True:
        day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or "all"?\n')
        if day in ["all"] + WEEK_LIST:
            ret_val = day
            break
        else:
            print("\nError input! Try Again?")
    return ret_val


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    city = get_city()

    """Ask for filter mode!"""
    filter_mode = get_filter_mode()
    if filter_mode=='both':
        month = get_month()
        day = get_day()
    elif filter_mode=='month':
        month = get_month()
        day = None
    elif filter_mode=='day':
        month = None
        day = get_day()
    else:# Here is for filter_mode "none"
        month = None
        day = None

    print('-'*40)
    return city, month, day

def dealwith_month(datetimestr):
    #	1 到 12
    #month_int = time.strptime(datetimestr, '%Y-%m-%d %H:%M:%S').tm_mon
    # 这里使用字符串截取的方式 更有效率
    month_int = int(datetimestr[5:7])
    return MONTH_LIST[month_int-1]

def dealwith_weekday(datetimestr):
    # 0到6 (0是周一)
    dayofweek_int = time.strptime(datetimestr, '%Y-%m-%d %H:%M:%S').tm_wday
    
    return WEEK_LIST[dayofweek_int]
    
def dealwith_df_datetime(df):
    monthSeries = df['Start Time'].apply(dealwith_month)
    df["Start_Month"] = monthSeries
    return df;

def dealwith_df_weekday(df):
    weekDaySeries = df['Start Time'].apply(dealwith_weekday)
    df["Start_Weekday"] = weekDaySeries
    return df;

def dealwith_hour(datetimestr):
    #hour_int = time.strptime(datetimestr, '%Y-%m-%d %H:%M:%S').tm_hour
    # 这里使用字符串截取的方式 更有效率
    hour_int = int(datetimestr[11:13])
    return hour_int

def dealwith_df_hour(df):
    hourSeries = df['Start Time'].apply(dealwith_hour)
    df["Start_Hour"] = hourSeries
    return df;

def load_data_from_cache_or_csv(city):
    ret_val = None
    """
    Use Dict cached pandas.DataFrame object.
    
    """
    print('\nStart loading data...\n')
    start_time = time.time()
    
    if city in CACHED_CITY_DATA.keys():
        ret_val = CACHED_CITY_DATA[city]
        print("load {} data from cache!".format(city))
    else:
        filename = CITY_DATA[city]
        ret_val = pd.read_csv(filename)
        # 对 起始时间进行预处理，处理出 开始月份
        dealwith_df_datetime(ret_val)
        # 对 起始时间进行预处理，处理出 开始的星期
        dealwith_df_weekday(ret_val)
        # 对 起始时间进行预处理，处理出 开始的小时
        dealwith_df_hour(ret_val)
        
        CACHED_CITY_DATA[city] = ret_val
        print("load {} data from file! Cached in Memory!".format(city))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    return ret_val

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
    
    df = load_data_from_cache_or_csv(city)
    
    if month in MONTH_LIST:
        df = df[df["Start_Month"]==month]
    
    if day in WEEK_LIST:
        df = df[df["Start_Weekday"]==day]
    
    print("There is {} line of data to calculate.".format(df.size))
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    if df.size>0:
        # display the most common month    
        most_common_month = df.groupby("Start_Month")["Start_Month"].count().idxmax()
        print("The most common month is {}".format(most_common_month))
        
        # display the most common day of week
        most_common_day = df.groupby("Start_Weekday")["Start_Weekday"].count().idxmax()
        print("The most common day of week is {}".format(most_common_day))
        
        # display the most common start hour
        most_common_hour = df.groupby("Start_Hour")["Start_Hour"].count().idxmax()
        print("The most common hour is {}".format(most_common_hour))
    else:
        print("Cannot share data abount The most commons about time!")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    if df.size>0:
        # display the most commonly used start station
        most_common_start_station = df.groupby("Start Station")["Start Station"].count().idxmax()
        print("The most commonly used start station is: {}".format(most_common_start_station))
        # display the most commonly used end station
        most_common_end_station = df.groupby("End Station")["End Station"].count().idxmax()
        print("The most commonly used end station is: {}".format(most_common_end_station))
        
        
        # display the most frequent combination of start station and end station trip
        most_common_pair_station = df.groupby(["Start Station", "End Station"])["Start Station", "End Station"].count().idxmax()
        print("The most frequent combination of start station and end station is {}".format(most_common_pair_station["Start Station"]))
    else:
        print("Cannot share data about The most commonly station!")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    if df.size>0:
        # display total travel time
        total_travel_time = df["Trip Duration"].sum()
        print("The Total travel time is {} seconds.".format(total_travel_time))
    
        # display mean travel time
        mean_travel_time = df["Trip Duration"].mean()
        print("The Mean of travel time is {} seconds.".format(mean_travel_time))
    else:
        print("Cannot share data abount Trip Duration Stats!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    if df.size>0:
        # Display counts of user types
        print("The counts of user types: ")
        print(df["User Type"].value_counts())
        
        if "Gender" in df.columns:
            # Display counts of gender
            print("The counts of gender: ")
            print(df["Gender"].value_counts())
        else:
            print("Cannot share Gender data!")
        
        if "Birth Year" in df.columns:
            # Display the earliest year of birth
            print("The most earliest year of birth is {}".format(df["Birth Year"].min()))
            # Display the most recent year of birth
            print("The most recent year of birth is {}".format(df["Birth Year"].max()))
            # Display thie most common year of birth
            most_common_year = df.groupby("Birth Year")["Birth Year"].count().idxmax()
            print("The most common year of birth is {}".format(most_common_year))
        else:
            print("Cannot share Birth Year data!")
    else:
        print("Cannot share data about User Type, Gender and Birth Year!")

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
    '''
    city = 'Chicago'
    month = None
    day = 'Friday'
    df = load_data(city, month, day)
    print(df.info())
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    '''