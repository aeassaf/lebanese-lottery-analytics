# importing the requests library
import requests
import os

dataset = ""

lotteryReulstCount = int(input("How many lottery draws are there? "))

for i in range(lotteryReulstCount + 1):
    # api-endpoint
    URL = "https://www.lldj.com/en/LatestResults/Loto?draw={0}".format(i)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, headers=headers)

    contentURL = r.text.split()

    result = ""

    counter = 0

    for content in contentURL:
        for j in range(43):
            if content == "ball-{0}\">{0}</li>".format(j):
                result += str(j)

                counter += 1
                if counter == 7:
                    result += "\n"
                else:
                    result += ", "

    dataset += result

    os.system("CLS")
    print("{0} out of {1}".format(i, lotteryReulstCount))

writeFile = open(
    "Lebanese Lottery #1-#{0}.csv".format(lotteryReulstCount), "w")

writeFile.write(dataset)

writeFile.close()
