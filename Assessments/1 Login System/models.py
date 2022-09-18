from functions import *


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __del__(self):
        pass

    def validUsername(self) -> bool:
        pattern = r"^[a-zA-Z][a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"  # email id checking regex pattern
        return isPatternMatch(pattern, self.username)

    def validPassword(self) -> bool:
        #  Password check Flags
        lengthFlag = False
        upperCaseFlag = False
        lowerCaseFlag = False
        digitFlag = False
        specialCharFlag = False

        #  Password length check
        if 5 < len(self.password) < 16:
            lengthFlag = True

        #  Uppercase characters availability check
        for char in self.password:
            if isPatternMatch('^[A-Z]', char):
                upperCaseFlag = True
                break

        #  Lowercase characters availability check
        for char in self.password:
            if isPatternMatch('^[a-z]', char):
                lowerCaseFlag = True
                break

        #  Digits availability check
        for char in self.password:
            if isPatternMatch('^[0-9]', char):
                digitFlag = True
                break

        #  Special characters availability check
        for char in self.password:
            if isPatternMatch(r'^[.@_!#$%^&*()<>?/\|}{~:]', char):
                specialCharFlag = True
                break

        #  Final check for valid password
        if lengthFlag & upperCaseFlag & lowerCaseFlag & digitFlag & specialCharFlag:
            return True
        else:
            return False

    def create(self) -> bool:
        print("User created successfully!!")
        return True
