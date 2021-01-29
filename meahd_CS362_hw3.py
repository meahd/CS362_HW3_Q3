# David Meah - CS361_HW1_Q4
# 1/29/21
# Leap year program checker with input validation

#Input validation function
def intInputValidation(user_input):
    while True: #Loops till right input is entered
        try:
            tempVal = int(input(user_input))
        except ValueError:
            print("Error: Invalid Input")
            print("Try again")
            continue
        else:
            return tempVal #If not ValueErrors then break out of loop
            break

#main function
year = intInputValidation("Input - ")

if(year % 4 == 0):
        if(year % 100 != 1):
            if(year % 400 == 0):
                print("Output -" ,year, " is a leap year")
            else:
                print("Output -" ,year, " is not a leap year")
        else:
            print("Output -" ,year, " is not a leap year")
else:
    print("Output -" ,year, "is not a leap year")
