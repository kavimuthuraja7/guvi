import json
from models import *
from functions import *

# Variables Declaration
InvalidcmdInfo = "Please enter the valid command using below reference!"  # Error text for invalid command
ExitInfo = "Bye, See you soon..!"  # Greetings text for exiting application
InvalidUsernameInfo = "Invalid Username format for registration, user registration aborted!"
InvalidPasswordInfo = "Invalid Password format for registration, user registration aborted!"
ConfirmPasswordErrorInfo = "Password and confirm password mismatched!, user registration aborted!"


# Main Loop
while True:
    printInfo()

    # getting user command
    cmd = input("Enter the command : ")

    # validating user command
    if not cmdCheck(cmd):
        print(InvalidcmdInfo)
        continue

    # command operations
    if cmd == '4':  # Exit operation
        break

    # Register Operation
    elif cmd == '1':
        printNewUserNameInfo()
        print("Type quit to exit from registration mode....")
        while True:
            newUser = User()  # New user creation
            # Getting username from user
            newUser.username = input("Please enter the username: ")

            if newUser.username.lower() == "quit":
                break
            # validating username
            if not newUser.validUsername():
                print(InvalidUsernameInfo)
                del newUser  # deleting created instance
                continue
            #  Getting password from user
            newUser.password = input("Please enter the password: ")
            if not newUser.validPassword():
                print(InvalidPasswordInfo)
                del newUser  # deleting created instance
                continue
            #  Getting confirm password from user
            confirmPassword = input("Confirm Password: ")
            if newUser.password != confirmPassword:
                print(ConfirmPasswordErrorInfo)
                del newUser
                continue

            newUser.create()
            break

    #  Login Operation
    elif cmd == '2':
        print("Type quit to exit from login mode....")
        while True:
            loginUserName = input("Username: ")  # Getting username from user
            if loginUserName.lower() == "quit":
                break
            # checking the username availability
            loginUser = User(username=loginUserName)
            if not loginUser.checkUsername():
                print("Invalid User ID")
                continue
            # checking password match
            loginUser.password = input("Password: ")
            if loginUser.login():
                print("User successfully logged in!")
                del loginUser
                break
            else:
                print("Invalid password")
                del loginUser

    #  Forgot Password Operation
    elif cmd == '3':

        forgotUser = User(username=input("Username: "))
        forgotUser.forgotPassword()

print(ExitInfo)
exit()
