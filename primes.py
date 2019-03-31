# Claire Nolan March 2019
# primes.py
# Question 5 of Problem Set
# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"
# specifically used section 4.4 of the Python tutorial


i = int(input("Please enter a positive integer: "))

for n in range(2, i):
    for x in range(2, n):
        if n % x != 0:
            print(n, 'is a prime number')
            break
    
# 1. Initial programme returned list from 3 to 18      