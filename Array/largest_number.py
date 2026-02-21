''' Find the Largest Element in an Array
    
    Time Complexity: O(n)
    Space Complexity: O(1)'''


def largestNumber(arr):

    n=len(arr)

    largest=arr[0]

    for i in range(n-1):
        if arr[i]>largest:
            largest=arr[i]
    
    return largest

arr=list(map(int,input().split()))
print(largestNumber(arr))