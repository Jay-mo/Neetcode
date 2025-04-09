"""
various deleting operations on an array

"""


myArray = [1,2,3,4,5]


#delete last element in an array

def removeEnd(arr,length):
    if length > 0:
        arr[length - 1] = 0
        length -= 1
    print(f"Array: {arr}, Array Length: {length}")

removeEnd(myArray.copy(),len(myArray))


print(myArray)

def removeMiddle(arr,index,length):
    for i in range(index+1,length):
        arr[i -1] = arr[i]
    arr[-1] = 0
    print(arr)
    

removeMiddle(myArray.copy(),0,len(myArray))