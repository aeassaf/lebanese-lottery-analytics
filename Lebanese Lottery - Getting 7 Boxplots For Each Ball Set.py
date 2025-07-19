import matplotlib.pyplot as plt
import numpy as np

totalDraws = 1797

def printFiveNumberSummary(dataToPlot):
    ##Q1 (25% -> .25), Q3 (75% -> .75) of the data
    Q1 = np.quantile(dataToPlot, .25)
    Q3 = np.quantile(dataToPlot, .75)
    
    print("The Five-Number Summary Is:\nMedian =",
      np.median(dataToPlot),
      "\nQ1 =", Q1,
      "\nQ3 =", Q3)

    ##IQR is Q3-Q2, 75%-25% = 50% -> .5
    IQR = np.quantile(dataToPlot, .5)

    ##Checking for possible outliers and removing them from being the maximum or the minimum
    ##A point is an outlier if it is higher than Q3/lower than Q1 by IQR*1.5
    minValue = dataToPlot[0]
    maxValue = dataToPlot[len(dataToPlot)-1]
            
    print("Minimum Value =", minValue,
          "\nMaximum Value =", maxValue)

##Read Lebanese Lottery #1-#1797.csv file, delimiter is to know how the data is seperated, dtype = None means it will take the data type dynamically
##names=True means it will ignore the names in the first row, encoding=None uses the default encoding method    
lotoDataFileContent = np.genfromtxt("Lebanese Lottery #1-#1797.csv", delimiter=',', dtype=None, encoding=None)

###In this section we are assigning all values of the 1st,2nd -> 7th colomns respectively to index 0,1,2 -> 6 of ballSetArray
###That way we get all values of ball1, all values of ball2, etc...
balls = []

for data in lotoDataFileContent:
    balls.append(data)

ballSetArray = [[], [], [], [], [], [], []]

for i in range(totalDraws):
    for j in range(7):
        ballSetArray[j].append(balls[i][j])

##sorting the arrays for quartile calculation purposes
for w in range(7):
    ballSetArray[w].sort()

##Output of the program should have 1 figure, having the left boxplot as slen and the right boxplot as plen
fig, axs = plt.subplots()

##plotting the data
axs.boxplot([ballSetArray[0], ballSetArray[1], ballSetArray[2], ballSetArray[3], ballSetArray[4], ballSetArray[5], ballSetArray[6]])

##Printing the five-number summary
for i in range(7):
    printFiveNumberSummary(ballSetArray[i])
    print("\n\n")

##Show Boxplots
plt.show()
