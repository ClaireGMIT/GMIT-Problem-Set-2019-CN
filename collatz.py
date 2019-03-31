# Claire Nolan March 2019
# collatz.py
# Question 4 of Problem Set
# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"

x = int(input("Please enter a positive integer: "))

while x > 1: 

    if x % 2 == 0: 
        x = x / 2 # ie if X is divisible by 2 then provide a new number which is the result of x divided by 2

    elif x % 2 != 0:
                x = (x*3)+1 # ie if X is not divisible by 2 then provide a new number which is the result of x multiplied by 3 plus 1

    print(int(x)) #print the list of values as integer


# 1: Initially getting as far as firtst step. Will look at indents. Have decided to remove "print (i)" command.  
# 2. Initial attempt just returned 5.0. Issue may be around getting correct indentation.
# 3. i'm going to restart and try "while" loops
# 4 Noticed my biggest problem is forgetting the : after each statement.
# 5. when i corrected and got a programme i get floating numbers. Fixed by using print(int(x))