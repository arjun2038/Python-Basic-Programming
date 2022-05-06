
#time
import time
print("Number of ticks",time.time())
print("struct_time",time.localtime())
print("formatted time:",time.asctime())

#calander
import calendar
print(calendar.month(2000,3))
print(calendar.firstweekday())
print(calendar.isleap(2001))
print(calendar.leapdays(2000,2008))

