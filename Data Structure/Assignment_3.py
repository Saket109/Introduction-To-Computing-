'''
    Question : We have Linear and Binary searches to search for elements in an array/list.


How would you search for an element in an array/list whose size is unknown?

Given:
1. Starting index of a sorted array/list
2. Your programming skills!

Hint:
1. Try to correlate the time complexity with element access times.
2. Binary search has O(log(n)) time complexity. (n is the number of elements)
3. Each step can also become a jump!
'''

# Code :

# We can use linear search without using the length of the sorted array but it will take
# O(n) time.

def linearSearch(arr,num):
    try:
        i = 0
        while True :
            if arr[i] == num:
                return i
            i += 1 
    except IndexError:
        return -1

# We can also use Binary search to find the number in the given sorted array without 
# using the lenght of the sorted array.
        # It will take only O(logn) time.

def binarySearch(arr,num,start=0,end=1):
    try :
        while arr[end] < num :
            start = end+1
            end = end*2

        return binarySearchHelper(arr,num,start,end)

    except IndexError:
        
        if end>start:
            end = (start+end)//2
            return binarySearch(arr,num,start,end)
        else:
            return -1 


def binarySearchHelper(arr,num,start,end):
    if start>end :
        return -1
    mid = (start+end)//2
    if arr[mid] == num :
        return mid
    if arr[mid] < num :
        return binarySearchHelper(arr,num,mid+1,end)
    else:
        return binarySearchHelper(arr,num,start,mid-1)  



# Main 
arr = [int(ele) for ele in input("enter the elements of the array separated by spaces : ").split()]
num = int(input("enter the number which you want to search : "))
print(linearSearch(arr,num))
print(binarySearch(arr,num))