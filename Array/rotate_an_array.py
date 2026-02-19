"""
Problem: Rotate array to the left by d steps

Approach (Reversal Algorithm):
1. Reverse first d elements
2. Reverse remaining elements
3. Reverse whole array

Time Complexity: O(n)
Space Complexity: O(1)
"""



def rotateAnArray(arr,d):

    n=len(arr)

    #handle the case where d>size of array
    d%=n

    #reverse the first d elements
    reverse(arr,0,d-1)

    #reverse the remaining n-d elements 
    reverse(arr,d,n-1)

    #reverse the entire elements
    reverse(arr,0,n-1)

def reverse(arr,start,end):

    while start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    

if __name__=="__main__":
    arr=list(map(int,input().split()))
    d=int(input())
    rotateAnArray(arr,d)

    for i in range(len(arr)):
        print(arr[i],end=" ")
