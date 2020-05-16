import requests
from random import sample as directory
from time import sleep, time
from timeit import timeit


startTime = time()


def generateLink(chars=None, length=None):
    chars = chars or "abcdefghijklmnopqrstuvwxyz0123456789"
    length = length or 6
    subdirectory = "".join(directory(chars, length))
    return f"https://prnt.sc/{subdirectory}"


def linkResponse(linkGeneration):
    response = requests.get(linkGeneration, headers={"user-agent": "Link Tester"})
    return (
        "//st.prntscr.com/2020/04/03/0204/img/0_173a7b_211be8ff.png"
        not in response.text
    )


def progressDisplay(percentagePart, percentageTotal):
    progressCalculation = int(percentagePart/percentageTotal*20)
    progressPercentage = int(percentagePart/percentageTotal*100)
    progressDisplay = "█"*progressCalculation
    print(f"GENERATING LINKS: {progressDisplay} {progressPercentage}%", end='\r')


def showStats(totalGenerated, executionTime, totalFound, totalDiscarded, totalDuplicated, successRate, linksList):
    print(f"\n==============================\n         -Statistics-\nLinks Scanned: {totalGenerated}\nExecution Time: {executionTime:.2f}s\nLinks Found: {totalFound}\nLinks Discarded: {totalDiscarded}\nLinks Duplicated: {totalDuplicated}\nSuccess Rate: {successRate}\n==============================\n")
    loadFile(linksList)


def loadFile(linksList):
    dataLoad = input("Would you like to load (L) the links or delete (D)? ")
    if dataLoad.lower() == "d" or dataLoad.lower() == "delete":
        print("Deleting Links From Storage...")

    elif dataLoad.lower() != "l":
        print("Invalid Input")
        loadFile(linksList)
    
    else:
        lineSplit = '\n'.join(linksList)
        print(lineSplit)


def main(linksList, linksAmount):

    linksList = []

    totalGenerated = 0
    totalFound = 0
    totalDiscarded = 0
    totalDuplicated = 0

    while totalGenerated < linksAmount:
        try:
            linkGeneration = generateLink()

            if linkResponse(linkGeneration):
                if linkGeneration in linksList:
                    totalDuplicated += 1

                else:
                    totalFound += 1
                    linksList.append(linkGeneration)

            else:
                totalDiscarded += 1

            totalGenerated += 1
            progressDisplay(totalGenerated, linksAmount)


        except KeyboardInterrupt:
            print("Paused Progress")
            pause = input("Enter Q to save progress and finish, anything else to continue: ")
            if pause.lower() == "q":
                print("Saving and finishing...\n")
                break

            else:
                continue

    print()
        
    sleep(0.1)
    successRate = (f"~{int(totalFound/totalGenerated*100)}%")
    executionTime = (time()-startTime)
    showStats(totalGenerated, executionTime, totalFound, totalDiscarded, totalDuplicated, successRate, linksList)


if __name__ == "__main__":
    linksAmount = int(input("How many links would you like to generate? "))
    main(linksAmount, linksAmount)
    input("Press enter to continue...")