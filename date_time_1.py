
import datetime

t = datetime.time(3,4,5)

print(t)
print(datetime.time(5,6,7))
print(datetime.time.max)
print(datetime.time.min)

print(datetime.time.resolution)

today = datetime.date.today()

print(today)

print(today.timetuple())

print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)


dob = datetime.date(2000,6,2)
today = datetime.date.today()

age = (today - dob)/365

print(age)
print(today - dob)


























