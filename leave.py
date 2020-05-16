from time import sleep


def shutdown():

    leaveConfirm = input("[LEAVE REQUEST] Confirm (Y/N) >>>")

    if leaveConfirm.lower() == "y":
        for i in range(0, 9):
            print("Goodbye!"[:i], end='\r')
            sleep(0.025)
        
        sleep(0.5)
        exit()

    else:
        print("[LEAVE REQUEST] No Confirmation")