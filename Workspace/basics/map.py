numberStrings = ['1', '2', '3']
numbers = list(map(int, numberStrings))
print(numbers)


def addHalf(inputValue):
    return inputValue+(inputValue*0.5)


newNumbers = list(map(addHalf, numbers))
print(newNumbers)

names = ['kavi', 'muthu', 'raja']
formattedNames = list(map(str.capitalize, names))
print(formattedNames)


def replace(stringarray=["", "", ""]):
    stringarray = stringarray[0].replace(stringarray[1], stringarray[2])
    return  stringarray


data = [["kavi$","$", "" ], ["Muthu@", "@", "$"]]

output = list(map(replace, data))
print(output)