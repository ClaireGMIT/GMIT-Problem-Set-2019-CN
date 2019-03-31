# Claire Nolan March 2019
# plot.py
# Question 10 of Problem Set
# Ref: Lecture Notes and Python Tutorial, coders apprentice, "python in easy steps" by Mike Mcgrath"
# Also ref: https://matplotlib.org/users/pyplot_tutorial.html and https://www.oreilly.com/library/view/python-data-science/9781491912126/ch04.html


import matplotlib.pyplot as plt
# import Mat lab function
import numpy as np
# Impurt numpy finction
x = range(1,4) # identified x from range 0 to 4 as per question
y = np.square(x) # use numpy to provide the square of x
z = np.multiply(x, 2) # use numpy to provide 2 times x

fig = plt.figure() # specieis type of grpah required
ax = fig.add_subplot(111)
ax.plot(x, y, z) # specifies that 3 axis
plt.show() # shows grapical results. 

#Note provides two graphs rather than one graph with 3 axes. I will have t investigate this more.


