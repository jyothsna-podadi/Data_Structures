"""
Problem: Move all zeros to the end of the array
while maintaining the order of non-zero elements

Time Complexity: O(n)
Space Complexity: O(1)
"""

def moveAllZerosToEnd(arr):

    #pointer to track the position
    count=0

    for i in range(len(arr)):

        #if the current element is not zero
        if arr[i]!=0:

            arr[i],arr[count]=arr[count],arr[i]

            count+=1
    

if __name__=="__main__":
    arr=list(map(int,input().split()))
    moveAllZerosToEnd(arr)

    for num in arr:
        print(num,end=" ")