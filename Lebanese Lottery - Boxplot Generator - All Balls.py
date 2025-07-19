import matplotlib.pyplot as plt
import numpy as np


def printFiveNumberSummary(dataToPlot):
    # Q1 (25% -> .25), Q3 (75% -> .75) of the data
    Q1 = np.quantile(dataToPlot, .25)
    Q3 = np.quantile(dataToPlot, .75)

    print("The Five-Number Summary Is:\nMedian =",
          np.median(dataToPlot),
          "\nQ1 =", Q1,
          "\nQ3 =", Q3)

    # IQR is Q3-Q2, 75%-25% = 50% -> .5
    IQR = np.quantile(dataToPlot, .5)

    # Checking for possible outliers and removing them from being the maximum or the minimum
    # A point is an outlier if it is higher than Q3/lower than Q1 by IQR*1.5
    minValue = dataToPlot[0]
    maxValue = dataToPlot[len(dataToPlot)-1]

    # Assigning min/max to the corresponding non-outlier point
    # Example if index 0 outlier, check index 1 for min, make sure that the next index is smaller than Q1_index
    # if the last index is an outlier check its previous index making sure that index is bigger than Q3_index
    if minValue < (Q1 - IQR*1.5):
        for i in range(int(len(dataToPlot)*0.25)):
            if dataToPlot[i] >= (Q1 - IQR*1.5):
                minValue = dataToPlot[i]
                break

    if maxValue > (Q3 + IQR*1.5):
        for i in range(len(dataToPlot)-1, int(len(dataToPlot)*0.75), -1):
            if dataToPlot[i] <= (Q3 + IQR*1.5):
                maxValue = dataToPlot[i]
                break

    print("Minimum Value =", minValue,
          "\nMaximum Value =", maxValue)


totalDrawCount = input("What is the total number of draws? >")
# Read iris-data.txt file, delimiter is to know how the data is seperated, dtype = None means it will take the data type dynamically
# names=True means it will ignore the names in the first row, encoding=None uses the default encoding method
lotoDataFileContent = np.genfromtxt(
    "Lebanese Lottery #1-#{0}.csv".format(totalDrawCount), delimiter=',', dtype=None, encoding=None)

# lists to store slen data and plen data
balls = []

for data in lotoDataFileContent:
    for d in data:
        balls.append(d)

# sorting the arrays for quartile calculation purposes
balls.sort()

# Output of the program should have 1 figure, having the left boxplot as slen and the right boxplot as plen
fig, axs = plt.subplots()

# plotting the data
axs.boxplot(balls)

# Printing the five-number summary
printFiveNumberSummary(balls)

# Show Boxplots
plt.show()
