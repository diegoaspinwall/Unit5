#Diego Aspinwall
#10-15-17
#displayDate.py

from datetime import *

day = date.today().day
month = date.today().month
year = date.today().year
weekday = date.today().weekday()

monthlist = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
weekdaylist = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

print('Today is', weekdaylist[weekday], ',', monthlist[month], day, year)
