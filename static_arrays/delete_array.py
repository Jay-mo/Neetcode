"""
various deleting operations on an array

"""


myArray = [1,2,3,4,5]


#delete last element in an array

def removeEnd(arr,length):
    if length > 0:
        arr[length - 1] = 0
        length -= 1
    print("Remove last element in array")
    print(f"Array: {arr}, Array Length: {length}")



#remove from middle or anywhere in the array

def removeMiddle(arr,index,length):
    if index >= length:
        print(f"Cannot not delete elem with index {index} , since it is greater than the length of array: {length}")
        print(arr)
        return
        
    for i in range(index+1,length):
        arr[i -1] = arr[i]
    arr[-1] = 0
    print(f"Remove element with index {index} in array")
    print(f"Array: {arr}")


#insert element into the end of array

def insertEnd(arr,elem, length, capacity):
    
    if length >= capacity:
        print(f"Cannot insert element into array. There is no space left")
        print(arr)
        return
    else:
        # print(type(arr))
        # print(arr)
        arr.extend([0] * (capacity - length))
        # print(type(arr))
        arr[length] = elem
        print(f"Insert {elem} into last position in array")
        print(arr)
    

#insert element into nth index
def insertMiddle(arr, index, elem, length):
    arr.extend([0])

    for i in range(length,index - 1,-1):
        arr[i] = arr[i-1]
    arr[index] = elem
    print(arr)
    pass


print(f" Initial array: {myArray}")


removeEnd(myArray.copy(),len(myArray))

removeMiddle(myArray.copy(),4,len(myArray))

insertEnd(myArray.copy(),10, 5, 10)

insertMiddle(myArray.copy(), 3, 10,len(myArray))

