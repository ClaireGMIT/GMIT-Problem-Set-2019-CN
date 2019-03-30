# Claire Nolan March 2019
# Python-divisors.py
# Question 3 of Problem Set
# Ref: Lecture Notes and Python Tutorial

n = 6

for x in range (1000 , 10000):
    while (x /= 6) :
        i = x /= 6
        print (int(i))
        break

Print ("This list are divisible by 6 but not by 12")


