from datetime import datetime,date

#using date class
dt1 = date(year=2025, month = 3, day = 10)
dt2 = date(year=2025, month = 2, day = 10)

diff_date = dt1 - dt2

print("No of days between 2 dates are:",diff_date)

# days and time differences

t1 = datetime(year=2025, month = 3, day = 10, hour = 12, minute = 15, second = 40)
t2 = datetime(year=2025, month = 2, day = 10, hour = 10, minute = 5, second = 30)

date_time_diff = t1 - t2
print("date and Time difference between 2 date",date_time_diff)

print(type(diff_date))
print(type(date_time_diff))

# time delta objects shows diff between 2 dates

# type of date type 
