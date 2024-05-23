import datetime as dt


now = dt.datetime.now()
date = input('Enter Date (yearr,month, day): eg(2024, 1, 31) :')
time = input('Enter Time(hrs, mins, secs): eg( 15, 30, 31) :')

set_alarm = dt.datetime(int(date), int(time))
print(set_alarm)
print(now)
