"""
Problem: Find the next lexicographical permutation

Time Complexity: O(n)
Space Complexity: O(1)
"""



def nextPermutation(arr):

    n=len(arr)

    #find pivot index
    pivot=-1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            pivot=i
            break
    
    #if pivot point does not exist, reverse the array
    if pivot==-1:
        arr.reverse()
        return
    
    #swap the element from right that is greater than pivot
    for i in range(n-1,pivot,-1):
        if arr[i]>arr[pivot]:
            arr[i],arr[pivot]=arr[pivot],arr[i]
            break
    
    #reverse the elements from pivot+1 to the end
    left,right=pivot+1,n-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1

if __name__=="__main__":
    arr=list(map(int,input().split()))
    nextPermutation(arr)

    print(" ".join(map(str,arr)))