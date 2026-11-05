# CONSTANTS
VALID_PIN = 6667
LENGTH = 3

# FUNCTIONS
def pin_checker(count, pin_length):

    while count != 0:
        PIN = int(input("Enter your pin: "))
        if len(str(PIN)) != pin_length:
            print("Incorrect Length, please retry.")
        else:
            if PIN != VALID_PIN and count != 1:
                count = count - 1
                print(f"Incorrect. You have {count} attempts left.")
            elif count == 1 and PIN != VALID_PIN:
                message = "No more attempts left. Quitting..."
                return message
            else:
                message = "Correct pin!"
                return message

#MAIN PROGRAM

print(pin_checker(3,4))
