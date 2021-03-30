myUniqueList = []
myLeftovers = []


def addItem(item):
    if (item in myUniqueList):
        myLeftovers.append(item)
        return False
    else:
        myUniqueList.append(item)
        return True


print(addItem('sth'))
print(addItem('test'))
print(addItem(44))
print(addItem(True))
print(addItem('test'))

print(myUniqueList)
print(myLeftovers)
