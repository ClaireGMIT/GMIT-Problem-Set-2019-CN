# Claire Nolan March 2019
# collatz.py
# Question 4 of Problem Set
# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"

x = int(input("Please enter an integer: "))

if x % 2 == 0:
    i = x / 2
    print(i)
      
if x % 2 != 0:
        i = (x*3)+1
        print(i)

              

# Initial attempt just returned 5.0
