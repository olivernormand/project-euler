"""
    Counting Sundays

    You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

    One method:
        Go through all the days from 1 Jan 1900 to 31 Dec 2000, give dd/mm/yyyy w
        Then count number where dd == 1 and w = 7
    Seems easiest.

    calendar = [[dd,mm,yyyy,w]]

    Months with 30:
        September9, April4, June6, November11
    Months with 31:
        January1, March3, May5, July7, August8, October10, December12


    Running from 1st Jan 1900 to 31st December 2000 we get 173
    Running from 1st Jan 1900 to 31st December 1900 we get 2
    Difference is 171 --> correct
"""
import time
t0 = time.time()

calendar = [[1,1,1900,1]]

def isleapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
def islastdayofmonth(date):
    # in general
    if date[0] < 28:
        return False

    # Months with 30
    if date[1] in [4,6,9,11]:
        if date[0] == 30:
            return True
        else:
            return False

    # Months with 31
    if date[1] in [1,3,5,7,8,10,12]:
        if date[0] == 31:
            return True
        else:
            return False

    # February
    if date[1] == 2:
        if isleapyear(date[2]):
            if date[0] == 29:
                return True
            else:
                return False
        else:
            if date[0] == 28:
                return True
            else:
                return False
def nextday(date):
    # Returns the next day following a given date

    # Day, Month and Year
    if islastdayofmonth(date):
        dd = 1
        mm = date[1] + 1
        if mm > 12:
            mm += -12
            yyyy = date[2] + 1
        else:
            yyyy = date[2]
    else:
        dd = date[0] + 1
        mm = date[1]
        yyyy = date[2]

    # Weekday
    w = date[3] + 1
    if w > 7:
        w += -7

    return [dd,mm,yyyy,w]


    pass

while calendar[-1][2] < 1901:
    # print(calendar[-1])
    calendar.append(nextday(calendar[-1]))
calendar.pop() # removes the first day of the new year

premiersundays = 0
for date in calendar:
    if date[0] == 1:
        if date[3] == 7:
            premiersundays += 1
print(premiersundays)
tf = time.time()
print(tf-t0)
