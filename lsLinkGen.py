import requests
from random import sample as directory
import time
import tools


def generateLink(chars=None, length=None):
    chars = chars or "abcdefghijklmnopqrstuvwxyz0123456789"
    length = length or 6
    subdirectory = "".join(directory(chars, length))
    return f"https://prnt.sc/{subdirectory}"


def linkResponse(linkGeneration):
    response = requests.get(linkGeneration, headers={"user-agent": "Link Tester"})
    return (
        "data:image/png;base64,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841644031Jtvvqk++OAD9fHHH6tPP/1Uffvtt9G/X3/9Vf3+++9qhhlmUPPPP7+ab7751NJLL6023nhjtckmm6g111yz9NX/+OOP6p577lGjRo1Sr7zyivrss8/UDz/8oH766Sc100wzqZlnnlnNOeec0XwWXHBBteSSS6pllllGrbbaamqttdZSrVu3Ln1ORTr8+++/1ciRI9Ujjzyixo0bp95//301ZcqUCLeUSJllllnUb7/95j3E66+/ru6///4IP++88476/PPP1S+//KLmmGOOCB+LLrqo2mCDDVTXrl1Vp06dIpzVEr7//nt16623qkcffVS99tpr6ssvv4zWM/fcc6vllltObbjhhmrfffdVK6+8snMa4OWuu+5SDz/8sJowYcK0vhZYYAHVtm1b1aVLF7XrrruqlVZaydlXngaTJ0+OaO+pp56K1jJp0iQFPQJzzTWXWnzxxdWqq64a0X737t2j8zA9Q6NpDTq688471QMPPKBefvnliBfwN2i9TZs2ql27dqpz585qp512ivZHh2YtmJZaain10UcfVSDkvvvuU//617+86ZUDi2DQYYkllqjqN61DGNW2225b0YS5IWzSwLZ53hNXSq2zzjrqtNNOU926dcvymbXtd999p0499VR13XXXRYw2L9SqHpZtPmnE/88//6hrrrlG9enTJxL2SdCyZUv1xx9/OJcLwzz33HPV2LFjnW3jBghtvtltt91Unr1OWx8KS9++fdWFF17o3C/62WeffdSgQYMipcKEv/76S51//vmqf//+kRKSBjPOOKM67LDDorFnn312b1ykNeQMn3nmmeqmm25Sf/75p1ef7Nuee+4Z7S9C0xdWX331SOjqcOKJJ6rzzjvPt4vEdvQDHnVo3769Gj9+fKa+G0Fr5gSHDh0a8YOvv/7aOXeE0vHHHx/9Q3EFmrVg6tWrl7r66qsrEHfkkUeqiy++2IlMGnzxxReJGv57770X3QR8gDEHDhxY0ZS5sblpkIdZ2frbe++91VVXXTWNKHzmrLd59tln1Q477KC4wRWFEAQTmj/CYMSIEc7lcKNJY4bcQGDq3LjyAjeou+++W3HzyAJJh5t9QhEaPXp0lu4iDffJJ5+Mbrsx0Nc222yjxowZk6mvTTfdVD344INqttlmy/SdjQEeddRR6ueff87VD4IWgcut0AfgDUcffXRF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"
        not in response.text
    )


def progressDisplay(percentagePart, percentageTotal):
    progressCalculation = int(percentagePart/percentageTotal*20)
    progressPercentage = int(percentagePart/percentageTotal*100)
    progressDisplay = "█"*progressCalculation
    print(f"GENERATING LINKS: {progressDisplay} {progressPercentage}%", end='\r')


def showStats(totalGenerated, executionTime, totalFound, totalDiscarded, totalDuplicated, successRate, linksList):
    print(f"\n==============================\n         -Statistics-\nLinks Scanned: {totalGenerated}\nExecution Time: {executionTime:.2f}s\nLinks Found: {totalFound}\nLinks Discarded: {totalDiscarded}\nLinks Duplicated: {totalDuplicated}\nSuccess Rate: {successRate}\n==============================\n")
    loadFile(totalGenerated, executionTime, totalFound, totalDiscarded, totalDuplicated, successRate, linksList)


def loadFile(totalGenerated, executionTime, totalFound, totalDiscarded, totalDuplicated, successRate, linksList):
    dataLoad = input("Would you like to load (L) the links or delete (D)? ")
    if dataLoad.lower() == "d" or dataLoad.lower() == "delete":
        print("Deleting Links From Storage...")
        tools.main("lightshot")

    elif dataLoad.lower() != "l":
        print("Invalid Input")
        loadFile(totalGenerated, executionTime, totalFound, totalDiscarded, totalDuplicated, successRate, linksList)
    
    else:
        lineSplit = '\n'.join(linksList)
        print(lineSplit)

        error = True

        while error:
            saveData = input("Would you like to save the data into a lsLinkDB.txt (S) or delete (D)? ")

            if saveData.lower() == "d":
                error = False
                print("Deleting Data...")
                tools.main("lightshot")
            
            elif saveData.lower() == "s":
                print("Saving Data...")
                stats = [totalGenerated, executionTime, totalFound, totalDiscarded, totalDuplicated, successRate]
                error = False
                saveFile(lineSplit, stats)
            
            else:
                print("Invalid Input")



def saveFile(data, stats):
    print("save")
    tools.main("lightshot")



def main(linksAmount):

    linksList = []

    startTime = time.time()
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
        
    time.sleep(0.1)
    successRate = (f"~{int(totalFound/totalGenerated*100)}%")
    finishTime = time.time()
    executionTime = finishTime - startTime
    showStats(totalGenerated, executionTime, totalFound, totalDiscarded, totalDuplicated, successRate, linksList)


if __name__ == "__main__":
    linksAmount = int(input("How many links would you like to generate? "))
    main(linksAmount)
    input("Press enter to continue...")
