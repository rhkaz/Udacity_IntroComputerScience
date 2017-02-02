### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
### assuming all days are 30 days long

# def nextDay(year, month, day):
#     if day < 30 :
#         return year, month, day + 1
#     # else :
#     #     if month < 12 :
#     #         return year, month + 1, 1
#     #     else :
#     #         return year + 1, 1, 1
#
# print nextDay(1999, 12, 30)
#
#
# def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#     """Returns the number of days between year1/month1/day1
#        and year2/month2/day2. Assumes inputs are valid dates
#        in Gregorian calendar, and the first date is not after
#        the second."""
#
#     # YOUR CODE HERE!
#     return
