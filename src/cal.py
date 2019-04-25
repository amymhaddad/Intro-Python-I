"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should 
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that 
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
#why bring in date time this way, and not just import datetime
#How to access and print datetime attributes, ie: datetime.year
from datetime import datetime, time

c = calendar.TextCalendar()

#Update else so it captures all non-ints; make sure it works with elif condition above 

def generate_calendar():

  while True:
    user_cal = input("Enter a month and year as numbers, separated by a space: ")
 
    if user_cal == '':
      current_month = datetime.now().month
      print("Current month:" , current_month)
      break

    elif len(user_cal) == 1:
      current_calendar = c.formatmonth(2019, int(user_cal))
      return current_calendar
      break
    
    elif len(user_cal) > 1:
      list_user_input = user_cal.split(" ")
      month = int(list_user_input[0])
      year = int(list_user_input[1])

      current_calendar = c.formatmonth(year, month)
      return current_calendar
      break

    else:
      print("Invalid input. Try again. \n")

print(generate_calendar())
