from datetime import date, datetime, time, timedelta

today = date.today()

print("today is:" , today)
print("day is:" , today.day)
print("month is:" , today.month)
print("year is:" , today.year)
# print date object info with string formatting codes
print(today.strftime("%A, %d, %B of %Y "))

next_year = today.replace(year = today.year + 1)
print(next_year)

# count down to a specific date
difference = abs(next_year - today)
print("only {} days until next year".format(difference.days))

Nikola_tesla = date(1856, 7, 10)
date.fromisoformat("1856-07-10")
print("Nikola Tesla was born on:", Nikola_tesla)
# print weekday  monday = 0 and sunday = 6
print(Nikola_tesla.weekday())

now = datetime.now()
print(now)
print("it's {}th minute of the {}th hour of the {}th day of the {}th month".format(
    now.minute,
    now.hour,
    now.day,
    now.month
))

chernobyl = datetime.fromisoformat("1986-04-26 01:23:40:000+04:00")
print(chernobyl.strftime("The Chernobyl disaster occurred on %A %dth %B of %Y at %X in the %Z timezone"))

my_time = time(11, 22, 34)
print(my_time)


# time delta

today = datetime.now()
tomorrow = today + timedelta(days=1)
yesterday = today + timedelta(days=-1)
print(tomorrow)
print(yesterday)
