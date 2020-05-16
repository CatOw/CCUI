from time import sleep
from os import system, name


def startupIntro():

    system('cls' if name == 'nt' else 'clear')

    for i in range(0, 48):
        print("[CCUI] Starting CatOw's Console User Interface..."[:i], end='\r')
        sleep(0.025)
    print()

    
    printCatOw = ["\n /\\__/\\"," |O  O|"," \\_^^_/","  /  \\______","  \\    <<   \\______/\\","   |   C   T   W    |","    \\____A___O_____/\n"]
    for i in printCatOw:
        print(i)
        sleep(0.1)