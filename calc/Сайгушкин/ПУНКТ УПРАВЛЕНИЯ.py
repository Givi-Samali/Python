import datetime
time_1, time_2 = map(str, input().split(' '))
h1, m1 = map(int, time_1.split(':'))
h2, m2 = map(int, time_2.split(':'))
time1 = datetime.time(h1, m1)
time2 = datetime.time(h2, m2)
time1 = datetime.datetime(2024, 12, 12, h1, m1)
time2 = datetime.datetime(2024, 12, 12, h2, m2)
if time2 < time1:
    time1, time2 = time2, time1
rtime = (time2 - time1)/2
print(str((time1 + rtime).time())[:-3])