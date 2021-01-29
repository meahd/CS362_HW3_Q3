# David Meah - CS361_HW1_Q4
# 1/15/21
# Leap year program checker

year = int(input("Input - "))

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
