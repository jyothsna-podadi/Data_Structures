''' Find Smallest number in the array. 
    
    Time Complexity: O(n)
    Space Complexity: O(1)'''


def smallesNumber(arr):
    
    smallest=arr[0]
    for i in range(len(arr)-1):
        if arr[i]<smallest:
            smallest=arr[i]
    return smallest

arr=list(map(int, input().split()))
print(smallesNumber(arr))