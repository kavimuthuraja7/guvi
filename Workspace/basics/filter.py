marks = [100, 200, 44, 22, 55, 101, 10.4, 100.1]


def isValidMarks(mark):
    if mark <= 100:
        return True
    else:
        return False


filteredMarks = list(filter(isValidMarks, marks))
print(filteredMarks)

