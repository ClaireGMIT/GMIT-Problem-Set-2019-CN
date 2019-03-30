# Claire Nolan March 2019
# Python-divisors.py
# Question 3 of Problem Set
# Ref: Lecture Notes and Python Tutorial

for n in range(1000 , 10000):

   for x in range(1000, n):

      if n % 6 == 0:
         if n % 12 != 0:
              print(n, "is divisible by 6 but not 12" ) 
              break
              
   



# For this problem i learnt to use the error message in CMDER and VSC to isentify where i was making errors especially syntax errors.
# a couple of answers i got incldued just 9998 which using a calculator was not correct. Another attmpet led to all numbers between 1000 and 10000 being printed.
# I finally got it. I should have been using the modulate symbol. Also i needed to add the break command otherwise it went into a spiraling loop.




