# Claire Nolan March 2019
# second.py
# Question 9 of Problem Set
# Ref: Lecture Notes and Python Tutorial (specifically section 7.2), coders apprentice, "python in easy steps" by Mike Mcgrath"

f = open("MobyDick.txt" , "r") # ie open this particular file for reading

with open('MobyDick.txt', 'r') as f:
    Line_number = 0 # this is the initial line number to start count from
 
    for line in f:
        Line_number+=1
        if Line_number % 2 == 0: #this is the remainder operator ie if the line number is divisible by 2 then it prints the line.
            print(line)




#1. I tried print(line[::2]) initially and the output was every second character. rather than line.
#2. i tried using Lines = f.splitlines(".") to separate lines by full stop but i got an eror message as per Q6.
# i got the following error message AttributeError: '_io.TextIOWrapper' object has no attribute 'splitlines'
#3. i googled 

f.close()
# ensures file is closed at the end of the program

