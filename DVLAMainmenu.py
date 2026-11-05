# this module/code is for the main menu of the DVLA program
quitChoice = False
quitChoice2 = False
choice = ""
choice2 = ""
answer = ""


def r_u_sure():
    print("Are you sure?")
    answer == input("Enter your answer (Y/N): ").upper()
    if answer == "Y":
        print("Quitting program...")
        return 'y'
    elif answer == "N":
        print("OK")
    else:
        print("Invalid Arguement.")


while quitChoice == False:

    print("-- MAIN MENU -- \n1. Check for valid licence plate \n2. Generate Licence plate \n3. Find age of car from licence plate \n4. Quit.")
    #quitChoice = True
    #get the users choice
    choice = input("Enter your choice: ")

    #when the user chooses the quit option, set quitChoice to True and this will exit the while loop
    if choice == "4":
        #r_u_sure()
        print("Are you sure?")
        answer = input("Enter y for yes ").upper()
        if answer == "Y":
            print("Quitting program...")
            quitChoice = True
        else:
            print("ok continue.")

    elif choice == "1":
        print("Option 1 has been chosen.")

    elif choice == "2":
        print("Option 2 has been chosen.")

    elif choice == "3":
        print("Option 3 has been chosen.")
        
    else:
        print("Invalid Arguement")
