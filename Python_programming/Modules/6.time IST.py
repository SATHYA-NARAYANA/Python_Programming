from datetime import datetime

dt = datetime.now()

#dt.strftime("%d:%m:%y")

date_time = dt.strftime("%d:%m:%y")

#dt.strftime("%I:%M:%S %p")

time_format = dt.strftime("%I:%M:%S %p")

print("Current date and time is ",date_time,time_format )
