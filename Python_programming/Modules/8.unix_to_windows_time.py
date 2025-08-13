import datetime
unix_timestamp = 171998179
# avove is unix time stamp

# convert unix time stamp to windows format

dt_time = datetime.datetime.fromtimestamp(unix_timestamp)

print(dt_time)

dt = dt_time.strftime('%d-%m-%y')
tim_e = dt_time.strftime("%H:%M:%S")

print(dt)
print(tim_e)

