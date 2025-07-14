Sympt = input("Please enter a digit from the selection above (1-4): ")

SymptList = Sympt.split()

for Sympt in SymptList:

    Sympt = int(Sympt)

    if Sympt == 1:
        print("Please go home and take a test home")
    elif Sympt == 2:
        print("Please go home and take a test home")
    elif Sympt == 3:
        print("Please go see a doctor")
    elif Sympt == 4:
        print("You are Covid Free")
    else:
        print("Please select from numbers 1-4 based on the symptoms above")
