# Claire Nolan March 2019
# squareroot.py
# Question 8 of Problem Set
# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"


number = input( "Please enter a positive number: " )
l = float( number )

x = input("Please give an estimate of square root: ")
estimate = float(x)



# use float data type rather than integer so can use decimal points
# Used Newton Square root lecture notes to prepare.
# Added inputs for number and estimate to allow programme to run.

rootof = l

while abs((estimate * estimate) - rootof) > 0.1:
    estimate -= ((estimate * estimate) - rootof) / (2 * estimate)


print( f"The approximate square rootof {number} is approximately {estimate}.")









