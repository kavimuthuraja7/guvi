import json
import re


# Command Information Print
def printInfo():
    print("""
    ############ Welcome to Login Management ###########################
    ##  1 : Register                                                  ##
    ##  2 : Login                                                     ##
    ##  3 : Forgot Password                                           ##
    ##  4 : Exit                                                      ##
    ####################################################################
    """)


# Command Information Print
def printNewUserNameInfo():
    print("""
    --------------------------------------------------------------------------
        1. username should not start with any numbers or special characters
        2. username should be in the format of proper email id
            ex: guviuser@gmail.com, guvi.user32@edu.net
        3. username should not be like in the below formats
            ex: @gmail.com, guviuser@.gmail.com
    --------------------------------------------------------------------------
    """)


# User command input validation
def cmdCheck(cmd) -> bool:
    if cmd in ('1', '2', '3', '4'):
        return True
    else:
        return False


# RegEx pattern match
def isPatternMatch(pattern, text) -> bool:
    if re.match(pattern, text):
        return True
    return False


def getUserData():
    UserDataPath = "UserData/UserData.json"
    with open(UserDataPath) as f:
        existingUserData = json.load(f)
    return existingUserData


def setUserData(newUserData):
    UserDataPath = "UserData/UserData.json"
    temp = getUserData()
    try:
        with open(UserDataPath, 'w+') as f:
            json.dump(newUserData, f)
        return True
    except:
        with open(UserDataPath, 'w+') as f:
            json.dump(temp, f)
        return False
