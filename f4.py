mylist = [4,45,2,5,6,7,8,9]
#search element 6

def searchElement(target):
    for i in range(len(mylist)):
        if target == mylist[i]:
            
            print("Element found at index no = ", i)
        
searchElement(7)
searchElement(4)



mylist = [4,45,2,5,6,7,8,9,10]
#search element 6

def searchElement(target):
    for i in range(len(mylist)):
        if target == mylist[i]:
            return i
    return -1
result = searchElement(10)
if result != -1:
    print("element found at index number = ",result)
else:
    print("element not found")

print("--------------------")


def searchElement(target):
    mylist = [6, 10, 15, 20]  # define your list here
    for i in range(len(mylist)):
        if target == mylist[i]:
            return i
    return -1
result = searchElement(10)
if result != -1:
    print('Element found at index number:', result)
else:
    print('Element not found')