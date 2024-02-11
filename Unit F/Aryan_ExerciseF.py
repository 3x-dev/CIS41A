'''
Aryan Singhal
CIS 41A   Winter 2024
Unit F, Exercise F
'''

def hello():
    """This function prints 'Hello World'.\n"""
    print("Hello World")

def main():
    hello()
    print(hello.__doc__)

    myList = list(range(3))
    printListElement(myList, 3)

    myInt = 3
    myList = [0, 1, 2]
    print(f"Original ID of myInt in main is {id(myInt)}")
    print(f"Original ID of myList in main is {id(myList)}")
    print(f"Original ID of myList's last element in main is {id(myList[-1])}")

    byVal(myInt)
    byRef(myList)

    print(f"ID of myInt in main after call to byVal is {id(myInt)}")
    print(f"ID of myList in main after call to byRef is {id(myList)}")
    print(f"ID of myList's last element in main after call to byRef is {id(myList[-1])}")

    print(f"myInt is now: {myInt}")
    print(f"myList is now: {myList}")

def printListElement(aList, index):
    try:
        print(aList[index])
    except IndexError:
        print("Error: bad index number.\n")

def byVal(aVar):
    print(f"Original ID of parameter in byVal {id(aVar)}")
    aVar += 7
    print(f"ID of parameter in byVal after change {id(aVar)}")

def byRef(aList):
    print(f"Original ID of parameter in byRef {id(aList)}")
    print(f"Original ID of parameter's last element in byRef {id(aList[-1])}")
    aList[-1] += 7
    print(f"ID of parameter in byRef after change {id(aList)}")
    print(f"ID of parameter's last element in byRef after change {id(aList[-1])}")

main()


'''
Execution results:

Hello World
This function prints 'Hello World'.

Error: bad index number.

Original ID of myInt in main is 140675018621232
Original ID of myList in main is 140675021779328
Original ID of myList's last element in main is 140675018621200
Original ID of parameter in byVal 140675018621232
ID of parameter in byVal after change 140675018621456
Original ID of parameter in byRef 140675021779328
Original ID of parameter's last element in byRef 140675018621200
ID of parameter in byRef after change 140675021779328
ID of parameter's last element in byRef after change 140675018621424
ID of myInt in main after call to byVal is 140675018621232
ID of myList in main after call to byRef is 140675021779328
ID of myList's last element in main after call to byRef is 140675018621424
myInt is now: 3
myList is now: [0, 1, 9]
'''