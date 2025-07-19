import matplotlib.pyplot as plt
import numpy as np

totalDraws = 1797

# Read Lebanese Lottery #1-#1797.csv file, delimiter is to know how the data is seperated, dtype = None means it will take the data type dynamically
# names=True means it will ignore the names in the first row, encoding=None uses the default encoding method
lotoDataFileContent = np.genfromtxt(
    "Lebanese Lottery #1-#1797.csv", delimiter=',', dtype=None, encoding=None)

# In this section we are assigning all values of the 1st,2nd -> 7th colomns respectively to index 0,1,2 -> 6 of ballSetArray
# That way we get all values of ball1, all values of ball2, etc...
balls = []

for data in lotoDataFileContent:
    balls.append(data)

ballSetArray = [[], [], [], [], [], [], []]

for i in range(totalDraws):
    for j in range(7):
        ballSetArray[j].append(balls[i][j])

# Output of the program should have 1 figure, having the left boxplot as slen and the right boxplot as plen
fig, ax = plt.subplots()

# plotting the data
ax.scatter(ballSetArray[4], ballSetArray[5])

# Naming the x and y axis
plt.xlabel("Ball 1")
plt.ylabel("Ball 2")


# Show Boxplots
plt.show()
