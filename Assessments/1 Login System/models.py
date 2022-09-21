from functions import *


class User:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.userData = getUserData()

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

        if self.username not in self.userData["userid"]:
            self.userData["userid"].append(self.username)
            self.userData["password"].append(self.password)
        else:
            print('User already exists!!!')
            return False

        setUserData(self.userData)

        print("User created successfully!!")
        return True

    def checkUsername(self):
        userData = getUserData()
        if self.username in userData["userid"]:
            return True
        else:
            return False

    def login(self):

        for i in range(len(self.userData["userid"])):
            username = self.userData["userid"][i]
            password = self.userData["password"][i]
            if self.username == username and self.password == password:
                return True, "User Successfully Logged In!"

        return False

    def forgotPassword(self):
        if self.checkUsername():
            for i in range(len(self.userData["userid"])):
                username = self.userData["userid"][i]
                password = self.userData["password"][i]
                if self.username == username:
                    print("Your password is '{}'".format(password))
                    if (input("Do you want to change your password? (y/n) : ")).lower() == "y":
                        self.password = input("Enter new password:")
                        if self.validPassword():
                            self.userData["password"][i] = self.password
                            if setUserData(self.userData):
                                print("Password changed successfully!")
                            else:
                                print("Password change failed!")
                        else:
                            print("Invalid password format!")

        else:
            print("User doesn't exists!")
