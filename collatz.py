# Claire Nolan March 2019
# collatz.py
# Question 4 of Problem Set
# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"

x = int(input("Please enter an integer: "))


if x % 2 == 0:
    i = (x/2)
#Initially getting as far as this step. Will look at indents. Have decided to remove "print (i)" command.  
        
elif x % 2 != 0:
            i = (x*3)+1
            print(i)

else:
    if x == 1:

break

# i'm going to restart and try "while" loops
# Initial attempt just returned 5.0. Issue may be around getting correct indentation.



