def dispList(theList):
    print("*" * len(theList))
    print(theList)
    print("*" * len(theList))

def addtoEnd(theList):
    x = input("What do you want to add to the end of the list (default = Eric the Cat? ") or 'Eric the Cat'
    theList.append(x)
    print("*" * len(theList))
    print(f"{x} added to the end of the list.")
    print("*" * len(theList))

def insertBeg(theList):
    x = input("What do you want to add to the beginning of the list (default = Eric the Cat)? ") or 'Eric the Cat'
    theList.insert(0, x)
    print("*" * len(theList))
    print(f"{x} added to the front of the list.")
    print("*" * len(theList))

def addatPos(theList):
    thisBool = True
    while thisBool:
        try:
            x = int(input("What index do you want to insert the new item at? "))
            while x <= -1 or x >= len(theList) + 1:
                try:
                    x = int(input(f"Please enter a valid index between 0 and {len(theList)}: "))
                except ValueError:
                    pass
            y = input(f"What would you like to insert at position {x} (default = Eric the Cat)? ") or 'Eric the Cat'
            print("*" * len(theList))
            theList.insert(x, y)
            print(f"{y} added at position {x}.")
            print("*" * len(theList))
            thisBool = False
        except ValueError:
            print("Please enter a valid index number.")
            pass

def delByName(theList):
    l4 = []
    y = 0
    num = 1
    listLength = len(theList)
    thisBool = True
    while thisBool:
        z = input("What item would you like to delete? ")
        if z.isdigit():
            z = int(z)
        for x, res in enumerate(theList):
            if isinstance(res, list): 
                for x in res:
                    l4.append(x)
            else:
                l4.append(res)
        if z in l4:
            thisBool = False
            while y < listLength:
                if isinstance(theList[y], list):
                    while z in theList[y]:
                        print("*" * len(theList))
                        print(f"Removing {num} instance(s) of {z} from the list.")
                        print("*" * len(theList))
                        theList[y].remove(z)
                        num += 1
                        if isinstance(theList[y], list):
                            listLength -= 1
                            break
                elif myList[y] == z:
                    del theList[y]
                    print("*" * len(theList))
                    print(f"Removing {num} instance(s) of {z} from the list.")
                    print("*" * len(theList))
                    listLength -= 1
                    num += 1
                    y -= 1
                y += 1
        else:
            print("*" * len(theList))
            print(f"{z} not found - Please enter an item from the following list.")
            print("*" * len(theList))
            print(theList)
            print("*" * len(theList))
            thisBool = True
        
def delFirstItem(theList):
    print("*" * len(theList))
    print(f"{theList[0]} removed from the beginning of the list.")
    print("*" * len(theList))
    del theList[0]

def delLastItem(theList):
    print("*" * len(theList))
    print(f"{theList[-1]} removed from the end of the list.")
    print("*" * len(theList))
    del theList[-1]

def delByPosition(theList):
    thisBool = True
    while thisBool:
        try:
            x = int(input("Enter the index of the value that you would like to delete: "))
            while x <= -1 or x >= len(theList):
                try:
                    x = int(input(f"Please enter a valid index between 0 and {len(theList) - 1}: "))
                except ValueError:
                    pass
            print("*" * len(theList))
            print(f"{theList[x]} at element {x} has been removed from the list.")
            print("*" * len(theList))
            del theList[x]
            thisBool = False
        except ValueError:
            print("Please enter a valid index number.")
            pass   

def showFirstItems(theList):
    thisBool = True
    while thisBool:
        try:
            x = int(input("How many elements from the begining of the list do you want to show? "))
            while x <= 0 or x >= len(theList) + 1:
                try:
                    x = int(input(f"Please enter a valid number between 1 and {len(theList)}: "))
                except ValueError:
                    pass
            print("*" * len(theList))
            print(theList[:x])
            print("*" * len(theList))
            thisBool = False
        except ValueError:
            print("Please enter a numberic value.")
            pass

def showLastItems(theList):
    thisBool = True
    while thisBool:
        try:
            x = int(input("How many elements from the end of the list do you want to show? "))
            while x <= 0 or x >= len(theList) + 1:
                try:
                    x = int(input(f"Please enter a valid number between 1 and {len(theList)}: "))
                except ValueError:
                    pass
            print("*" * len(theList))
            print(theList[-x:])
            print("*" * len(theList))
            thisBool = False
        except ValueError:
            print("Please enter a numberic value.")
            pass

def checkItem(theList):
    l3 = []
    thisBool = True
    while thisBool:
        z = input("Enter item in the list: ")
        if z.isdigit():
            z = int(z)
        for x, res in enumerate(theList):
            if isinstance(res, list): 
                for x in res:
                    l3.append(x)
            else:
                l3.append(res)
        if z in l3:
            print("*" * len(theList))
            print("Found Item!")
            print("*" * len(theList))
            thisBool = False
        else:
            print(f"{z} is not in the list - Please try again.")
            thisBool = True

def addEric(theList):
    thisBool = True
    while thisBool:
        try:
            x = int(input("What index do you want to insert Eric at? "))
            while x <= -1 or x >= len(theList) + 1:
                try:
                    x = int(input(f"Please enter a valid index between 0 and {len(theList)}: "))
                except ValueError:
                    pass
            theList.insert(x, 'Eric')
            print("*" * len(theList))
            print(f"Eric has been added to the list at position {x}.")
            print("*" * len(theList))
            thisBool = False
        except ValueError:
            print("Please enter a valid index number.")
            pass       
                    
def menu(myList, choice):
    while True:
        try:
            while choice != 13:
                print("1 display the list")
                print("2 add an item to the list at the end")
                print("3 add an item to the list at the start")
                print("4 add an item to the list in a certain position")
                print("5 delete an item from the list by name")
                print("6 delete the first item")
                print("7 delete the last item")
                print("8 delete an item by position")
                print("9 show the first N items")
                print("10 show the last N items")
                print("11 check if an item is in the list")
                print("12 Add a cat named Eric to the list.")
                print("13 Exit")
                choice = int(input("Your choice: "))

                if choice == 1:
                    dispList(myList)
            
                elif choice == 2:
                    addtoEnd(myList)

                elif choice == 3:
                    insertBeg(myList)
            
                elif choice == 4:
                    addatPos(myList)
            
                elif choice == 5:
                    delByName(myList)
            
                elif choice == 6:
                    delFirstItem(myList)
            
                elif choice == 7:
                    delLastItem(myList)
            
                elif choice == 8: 
                    delByPosition(myList)
                
                elif choice == 9:
                    showFirstItems(myList)
                
                elif choice == 10:
                    showLastItems(myList)
                
                elif choice == 11:
                    checkItem(myList)
                
                elif choice == 12:
                    addEric(myList)
                
                elif choice == 13:
                    exit()
                
                if choice > 13:
                    print("************************************")
                    print("Please enter a valid menu number.")
                    print("************************************")
                
                if choice <= 0:
                    print("************************************")
                    print("Please enter a valid menu number.")
                    print("************************************")
        except ValueError:
            pass
        print("************************************")
        print("Please enter a valid choice.")
        print("************************************")

myList = ['toward', 18597, 'clear', 'last', 'task', 
        'family', 'leader', 'say', 'indicate', 'military', 
        'hit', 'available', 'equal', 'find', ['purple', 'needle', 7895, 'clearly'], 
        'forty', 'inside', ['during', 'very', 'pilot', 'region'], 'seems', 'discover']

choice = 0

if __name__=='__main__':
    menu(myList, choice)
