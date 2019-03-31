# Claire Nolan March 2019
# datetime.py
# Question 8 of Problem Set
# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"
# specifically used the standard library section of the Python tutorial


import datetime
now = datetime.datetime.now()
print ("Today is",now.strftime("%A, %B %d %Y at %H:%M:%S"))



# Error message at first attempt errors in line 7 and 8. Seems to be an error withte h datetime import. Why?
# Have tried code outside of this programme (via https://www.w3resource.com/python-exercises/python-basic-exercise-3.php) and i know it works. this is the error message {Traceback (most recent call last):File "datetime.py", line 8, in <module> from datetime import * File "C:\Users\Claire Laptop\Desktop\Programming\Problem-Set-2019-CN\datetime.py", line 10, in <module> now = datetime.datetime.now() NameError: name 'datetime' is not defined}
# I think the issue is to do with how and where the datetime is being imported from. I'm going to leave this as is for the moment and comeback to it


