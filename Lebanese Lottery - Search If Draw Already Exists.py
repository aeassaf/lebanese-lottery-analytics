import numpy as np

lotoDataFileContent = np.genfromtxt(
    "Lebanese Lottery #1-#1797.csv", delimiter=',', dtype=None, encoding=None)

# lists to store slen data and plen data
balls = []

for data in lotoDataFileContent:
    balls.append(data)

sortedBalls = []

for b in balls:
    tmpWithExtraBall = list(b)
    tmpWithoutExtraBall = tmpWithExtraBall[:len(tmpWithExtraBall)-1]
    tmpWithoutExtraBall.sort()
    sortedBalls.append(tmpWithoutExtraBall)


flag = 0

shouldContinue = 1

while(shouldContinue == 1):
    balls = input(
        "Check if your set of 6 numbers represents a draw (One space Between Numbers): ")

    listInputBalls = balls.split()

    while len(listInputBalls) < 6:
        balls = input(str(len(listInputBalls)) +
                      " balls were entered, we need 6 (re-input): ")
        listInputBalls = balls.split()

    for i in range(6):
        listInputBalls[i] = int(listInputBalls[i])

    listInputBalls.sort()

    for b in sortedBalls:
        if listInputBalls == b:
            print("FOUND!")
            flag = 1
            break

    if flag == 0:
        print("Not Found")

    shouldContinue = int(input(
        "Would You Like To Run Another Seach? Type 1 For Yes, Any Other Number Is Considered A No: "))
