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

import calendar
from string import ascii_letters as letters
from datetime import datetime, time

c = calendar.TextCalendar()

def generate_calendar():
  """Write a program that generates a calandar based on user input"""

  while True:
    user_cal = input("Enter a month and year as numbers, separated by a space: ")
    contains_letters = bool([letter for letter in user_cal if letter in letters])

    if contains_letters == True:
      print("Invalid input. Try again. \n")

    else: 
      if user_cal == '':
        print("Current month:" , datetime.now().month)
        break

      elif len(user_cal) == 1:
        return c.formatmonth(2019, int(user_cal))
        break
      
      elif len(user_cal) > 1:
        list_user_input = user_cal.split(" ")
        month = int(list_user_input[0])
        year = int(list_user_input[1])
      
        return c.formatmonth(year, month)
        break
    
print(generate_calendar())
