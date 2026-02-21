''' Find Second Smallest Number in the array. 
    
    Time Complexity: O(n)
    Space Complexity: O(1)'''


def SecondSmallestNumber(arr):

    n=len(arr)

    smallest=arr[0]
    second_smallest=arr[0]

    for i in range(n-1):
        if arr[i]<smallest:
            second_smallest=smallest
            smallest=arr[i]
        
        elif smallest<arr[i] and arr[i]<second_smallest:
            second_smallest[i]
    return second_smallest

arr=list(map(int,input().split()))
print(SecondSmallestNumber(arr))