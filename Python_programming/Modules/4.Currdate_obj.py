 # extract day, month year from date

from datetime import date

dt = date.today()
cur_day = dt.day
cur_year = dt.year
cur_month = dt.month

print(f'Current day:{cur_day}\nCurrent month:{cur_month}\nCurrent year:{cur_year}')
