"""
To read all the elements of an array.

Time Complexity: O(n)
"""


#initialize array
myArray = [1,2,3,4,5]

#Just learning how to use decorators.
def print_newline(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("\n")
    return wrapper

@print_newline
def traverse(arr):
    for i in arr:
        print(i,end='')
traverse(myArray)

@print_newline
def traverse_range(arr):
    for i in range(len(arr)):
        print(arr[i],end='')

traverse_range(myArray)

@print_newline
def traverse_while(arr):
    index = 0 
    length = len(arr)
    while index < length:
        print(arr[index], end="")
        index += 1

traverse_while(myArray)