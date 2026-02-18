"""
Problem: Reverse an array in-place

Time Complexity: O(n)
Space Complexity: O(1)
"""

def reverseAnArray(arr):

    n=len(arr)

    for i in range(n//2):

        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]


if __name__=="__main__":
    arr=list(map(int,input().split()))
    reverseAnArray(arr)

    for num in arr:
        print(num,end=" ")