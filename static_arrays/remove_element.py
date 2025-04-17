"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.


Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


"""
myArray = [1,2,3,4,5,0,0,0]

def insert_middle(arr,index,elem,length):
    for i in range(length -1,index,-1):
        arr[i] = arr[i - 1]
    arr[index] = elem
    print(arr)


def shift_elem_right(arr):
    for i in range(len(arr) - 1,0,-1):
        arr[i] = arr[i - 1]
    arr[0] = 0
    print(arr)

    
def shift_elem_left(arr):
    for i in range(len(arr) - 1):
        arr[i] = arr[i+1]
    arr[-1] = 0
    print(arr)


"""
I am going to write a function that takes an elem or an index 
and shifts that element to the end of the array.
"""


def shift_elem_to_end(arr,index):
    valueStore = arr[index]
    if index == len(arr) - 1:
        print(arr)
        return
    else:
        for i in range(index,len(arr) - 1):
            arr[i] = arr[i + 1]
        arr[-1] = valueStore
        print(arr)


def remove_element(arr,elem):
    lengthArray = len(arr)
    for i in range(lengthArray):
        while arr[i] == elem:
            shift_elem_to_end(arr,i)
            if array_all_the_same(arr[i:],elem):
                break

            
    count = 0
    for i in range(lengthArray):
        if arr[i] == elem:
            break
        else:
            count += 1
    print(f"array: {arr}, k = {count}")


def array_all_the_same(arr,elem):
    length = len(arr)
    for i in range(length):
        if arr[i] != elem:
            return False
    return True
    


# print(myArray)
# insert_middle(myArray.copy(),2,10,len(myArray))
# shift_elem_right(myArray.copy())
# shift_elem_left(myArray.copy())
# shift_elem_to_end(myArray.copy(),2)
remove_element([0,1,2,2,2,2,2,3,0,4,2],2)