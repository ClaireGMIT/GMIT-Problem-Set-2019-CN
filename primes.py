# Claire Nolan March 2019
# primes.py
# Question 5 of Problem Set
# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"
# specifically used section 4.4 of the Python tutorial


i = int(input("Please enter a positive integer: "))

for x in range(2 , i):
    if i % x == 0:
        print(i, "is not a prime number")
        break
            
else:
    if i % x != 0:
        print(i, "is a prime number")

# 1. Initial programme returned list from 3 to 18      
# 2. I need to get used to using the right symbols ie (, :) etc in the right places.
# 3. Realised i had the order wrong for the if and else statements. Once fixed program ran smoothly
