# Claire Nolan March 2019
# begins-with-t.py
# Question 2 of Problem Set
# Ref: Lecture Notes and Python Tutorial

import datetime # import todays date from module date and time module in puthon

if datetime.datetime.today().weekday() == 1: # states that if today is Tuesday (ie 1) then give the output that today begins with T
  print("Today begins with T")


if datetime.datetime.today().weekday() == 3: # states that if today is Thursday (ie 3) then give the output that today begins with T
  print("Today begins with T")

else:
  print("Today does NOT begin with T") # otherwise state that today doesn't begin with a T

# It took a while to figure this out but i re-watched the tutorials and figured it out. It probably could be simplified by copying/repeating some of the programme. I'll fine tune this later.