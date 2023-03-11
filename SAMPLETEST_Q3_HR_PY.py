def findMedian(arr):
    arr.sort()
    c = int((len(arr)-1)/2)
    return(arr[c])

arr = [1,3,2]
print(findMedian(arr))
