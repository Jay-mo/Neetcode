
def removeElement(arr,val):
    k = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[k] = arr[i]
            k += 1
    return (arr,k)





def removeElement2(arr,val):
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == val:
            n -= 1
            arr[i] = arr[n]
        else:
            i += 1
    return (arr,n)

print(removeElement2([0, 1, 2, 2, 2, 2, 3, 0, 4, 2, 2],2))