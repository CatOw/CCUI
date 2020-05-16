from time import sleep
from launchMessage import startupIntro
from help import helpMain as help
from help import helpCommand
from leave import shutdown
from reset import programReboot as reboot
from tools import main as tool
import lsLinkGen as lightshot


startupIntro()
CCUImain = True


def main():

    commandsList = ["shutdown", "help", "help tool", "tool lightshot", "reboot"]

    consoleInput = input("[CCUI/main]>>>")

    try:
        oldConsoleInput = consoleInput
        consoleInput = consoleInput.split()
        consoleInputLen = len(consoleInput)

        if consoleInputLen < 2 and consoleInput[0] in commandsList:
            eval(consoleInput[0]+"()")

        if consoleInputLen > 1 and oldConsoleInput in commandsList:
            if consoleInput[0] == "tool":
                tool(consoleInput[1])

            if consoleInput[0] == "help":
                helpCommand(consoleInput[1])
        
        elif consoleInputLen > 2 or oldConsoleInput not in commandsList:
            inputFail(oldConsoleInput)
        

    except IndexError:
        main()


def inputFail(failedCommand):
    print(f"[CCUI/main] ERROR: '{failedCommand}' is not a valid command or program. Type 'help' for usage.")


while CCUImain:
    main()