import tools


shutdownHelp = "shutdown       Shuts down the terminal."
toolHelp = "tool           Activate and use a tool or a program."
rebootHelp = "reboot         Restart the program."
toolLightshot = "tool lightshot      Activate the Lightshot Links Generator Tool and use it."

def helpMain():
    print("\nFor more information about specific commands type 'help command-name'.\n")
    print(f"{shutdownHelp}\n{toolHelp}\n{rebootHelp}\n")


def helpCommand(command):
    print("\nFor more information about specific commands type 'help command-name'.\n")
    
    if command == "tool":
        print(f"{toolLightshot}\n")


def helpTool(tool):
    print("\nFor more information about specific commands type 'help command-name'.\n")

    if tool == "lightshot":
        print("generate {number}     Generate a given amount of Lightshot Links to access images.\n")
        tools.main("lightshot")
