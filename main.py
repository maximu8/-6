#This program is meant to troubleshoot problems with a Wi-Fi connection
#It will go through steps telling the user a possible solution
#If replies "yes" then the program will reply "all done"
#If replies"no" then the program will reply with the next step to figue out the solution
reply = ""
print("Reboot the computer and try to connect.")
reply = input("Did that fix the problem?")
if reply == "yes":
    print("all done")
elif reply == "no":
    print("Reboot the router and try to connect.")
    reply = input("Did that fix the problem?")
    if reply == "yes":
        print("all done")
    elif reply == "no":
        print(
            "Make sure the cables between the router and modem are plugged in firmly."
        )
        replay = input("Did that fix the problem?")
        if reply == "yes":
            print("all done")
        elif reply == "no":
            print("Move the router to a new location.")
            reply = input("Did that fix the problem?")
            if reply == "yes":
                print("all done")
            elif reply == "no":
                print("You will need to get a new router")
