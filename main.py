from string import punctuation


def userName():
    uname = input("Please enter a username: ")
    while len(uname) <= 8 or not any (char.isupper() for char in uname):
            uname = input(f"Invalid username length. The username must be 8 characters long. Please enter a valid username: ")

    print(f"Welcome, {uname}! Your username is valid.")

def Password():
    special_char = list(punctuation)

    password = input("Please enter a password:")
    while len(password) <= 12 or not any(char in special_char for char in password) or not any (char.isupper() for char in password):
        password = input("Please enter a valid password with atleast 12 characters and special letters:")

    print("Your password is valid.")

def choice():

    print("Welcome to the program. Please Select from the symptoms below:")
    print("")
    print("1. Muscle Aches, Headaches, Loss of Appetite, and Loss of Taste or smell.")
    print("2. Dizzness and Fever")
    print("3. Runny Nose, Sore throat and Chills")
    print("4. Nothing hurt")

def userInput():
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


def main():

    print (" Hello Welcome to my symptom Checker")
    print (" Please Fill up the information and make and account")

    fname = input("Please Enter Your First Name:")
    lname = input("Please Enter Your Last Name:")
    age = input("Please Enter Your Age:")

    userName()
    Password()
    choice()
    userInput()

if __name__ == "__main__":
    main()


