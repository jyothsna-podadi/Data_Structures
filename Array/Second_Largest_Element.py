'''                 SECOND LARGEST ELEMENT IN AN ARRAY            '''


'''Given an array of positive integers arr[] of size n, the task is to find second largest distinct element in the array.
NOTE: If the second largest element does not exist, return -1'''



"""
Approach:
1. Traverse the array once
2. Track largest and second largest values
3. Update values accordingly

Time Complexity: O(n)
Space Complexity: O(1)

"""


#Function to find the second largest element
def getSecondLargest(arr):

    largest=-1
    second_largest=-1

    for i in range(len(arr)):
        if arr[i]>largest:
            second_largest=largest
            largest=arr[i]
        
        elif arr[i]<largest and arr[i]>second_largest:
            second_largest=arr[i]
    return second_largest

if __name__=="__main__":
    arr=list(map(int,input().split()))
    print(getSecondLargest(arr))
