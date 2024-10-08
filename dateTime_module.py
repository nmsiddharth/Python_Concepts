import datetime

mytime = datetime.time(2,20,45)
print(mytime)

today = datetime.date.today()
print(today)
print(today.day)

print(today.ctime())

mydateTime = datetime.datetime(2021,10,3,14,20,45)
print(mydateTime)

print(mydateTime.replace(year=2024))

#DATE
d1 = datetime.date(2025,9,22)
d2 = datetime.date(2024,9,22)

res = d1-d2
print(res)
