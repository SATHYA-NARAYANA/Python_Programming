from datetime import datetime

# Displaying date and time

dt = datetime.now()
print(dt)

# display date in 
dt1 = dt.strftime("%d-%m-%y")
print("Date:",dt1)

# display date (Date 31-Jul-2025)
dt2 = dt.strftime('%d-%h-%Y')
print("Date",dt2)

#display current time (Current Time 09:52:26)
dt3 = dt.strftime("%H:%M:%S")
print("Current Time",dt3)

# display date in Current data and time: (31-07-25 09:52:26)
dt4 = dt.strftime("%d-%m-%y %H:%M:%S")
print("Current data and time:",dt4)
